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
from .tasks import greet


from django.contrib.auth import get_user_model
MyUser = get_user_model()

# Create your views here.
def TeacherRole(user):
    return user.role==MyUser.Role.TEACHER


def login_view(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = MyUser.objects.filter(username=username)
            if not user.exists():
                messages.error(request, "Error! Username does not exist.")
                return redirect('login')

            print('----------- Login Start ------------') 
            print(username)
            print(password)
            print(user)
            print('------------ Login End -------------')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.role == MyUser.Role.TEACHER:
                    login(request, user)
                    messages.success(request, 'Success! You have logged in.')
                    return redirect(request.GET.get('next',"home"))
                else:
                    messages.error(request, 'Error! You are not authorized to log in.')   
            else:
                messages.error(request, 'Error! Passwords do not match.')



    except Exception as e:
        messages.error(request, 'Error! Something went wrong.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Success!, You have logged out.')
    return redirect('login')

def celery_view(request):
    print('-'*100)
    try:
            
        res = greet.delay()
        print(res)

        result = greet.delay()
        print(result.id)          # UUID
        print(result.status)      # e.g. PENDING, STARTED, SUCCESS, FAILURE
        print(result.get())
    except Exception as e:
        print(e)
        
    print('-'*100)
    return HttpResponse('Success')

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
    
    students = Student.objects.all().order_by('-id')
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

            student_exists = Student.objects.filter(name=name, subject=subject).exclude(id=pk).first()
            if student_exists:
                messages.error(request, 'Error! Student already exists.')
            else:
                student.name = name
                student.subject = subject
                student.mark = mark
                student.save()
                messages.success(request, 'Success! Student record updated')
            
        except Exception as e:
            messages.error(request, 'Failed to update student')
    
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