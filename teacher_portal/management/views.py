from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Student
from .filters import StudentFilter


from django.contrib.auth import get_user_model
MyUser = get_user_model()

# Create your views here.
def TeacherRole(user):
    return user.role==MyUser.Role.TEACHER


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # logger.info(f'Login attempt for username - {username}')

        user = MyUser.objects.filter(username=username)
        # if not user.exists():
        #     # logger.warning(f'User not found - {username}')
        #     messages.error(request, 'Error! User not found. Please try again.')
        #     return redirect('login')


        print('----------- Login Start ------------') 
        print(username)
        print(password)
        print(user)
        print('------------ Login End -------------')

        user = authenticate(username=username, password=password)

        if user is not None:
            # logger.info(f'User authenticated - {username}')

            # print(f"TENANT of Request : {request.tenant}")
            # print(f"TENANT of User : {user.tenant}")


            # Recapcha authentication.
            # SITE_KEY = request.POST['g-recaptcha-response']
            # capchaData = {
            #     'secret': settings.RECAPTCHA_PRIVATE_KEY,
            #     'response': SITE_KEY
            # }

            post_url = 'https://www.google.com/recaptcha/api/siteverify'

            try:
                # res = requests.post(post_url, data=capchaData)
                # verify = res.json()['success']
                # logger.info(f'INFO : reCAPTCHA verification result - {verify}')

                # if verify:
                if True:
                    if user.role == MyUser.Role.TEACHER:
                        login(request, user)
                        return redirect(request.GET.get('next',"home"))                    

                else:
                    logger.warning(f'Invalid reCAPTCHA for user - {username}')
                    messages.error(request, 'Error! Invalid Captcha. Please try again.')

            except Exception as e:
                # logger.error(f'Something went wrong - [Login from a Specific Tenant not Public] {str(e)}')
                messages.error(request, 'Error! Something went wrong.')
        


    contexts = {
        # 'RECAPTCHA_PUBLIC_KEY':settings.RECAPTCHA_PUBLIC_KEY 
    }
    return render(request, 'login.html', contexts)


def logout_view(request):
    logout(request)
    messages.success(request, 'Success!, You have logged out.')
    return redirect('login')


# #--------------------------------------- category Start ------------------------
@login_required(login_url='/')
def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        mark = request.POST.get('mark')

        student = Student.objects.filter(name=name, subject=subject).first()

        if student:
            student.mark=mark
            student.save()

            messages.success(request, 'Success! Student marks updated.')
        else:
            Student.objects.create(name=name, subject=subject, mark=mark)
            messages.success(request, 'Success! Student new record created.')
            
        return redirect('home')
    
    students = Student.objects.all().order_by('id')
    subjects = Student.objects.values_list('subject', flat=True).distinct()
    
    student_filter = StudentFilter(request.GET, queryset=students)

    # Pagination.
    page = request.GET.get('page', 1)
    paginator = Paginator(student_filter.qs, 10)
    try:
        page_items = paginator.page(page)
    except PageNotAnInteger:
        page_items = paginator.page(1)
    except EmptyPage:
        page_items = paginator.page(paginator.num_pages)

    contexts = { 
        'filter':student_filter, 
        'page_items':page_items,
        'subjects':subjects
          }
    
    return render(request, 'home.html', contexts)


# ----------------------------------- Student record update -----------------------------------
@require_http_methods(["POST"])
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        try:
            name = request.POST.get('name')            
            subject = request.POST.get('subject')            
            mark = request.POST.get('mark')

            student_exists = Student.objects.filter(name=name, subject=subject).first()
            if student_exists:
                messages.error(request, 'Error! Student already exists.')
            else:
                student.name = name
                student.subject = subject
                student.mark = mark
                student.save()
                messages.success(request, 'Success! Student record updated')
            
        except Exception as e:
            messages.error(request, 'Failed to update category name')
    
    return redirect('home')


# ----------------------------------- Student record delete -----------------------------------
def student_delete(request, pk):
    try:
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        
        messages.success(request, f'Success! Student record deleted.')
        
    except Exception as e:
        messages.error(request, 'Error! Student record delete failed')
    return redirect('home')