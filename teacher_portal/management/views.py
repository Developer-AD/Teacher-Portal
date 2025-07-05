from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
MyUser = get_user_model()
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse


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
    
    # category = Category.objects.all()
    # category_filter = CategoryFilter(request.GET, queryset=category)
    # cate=category_filter.qs

    # # Pagination.
    # page = request.GET.get('page', 1)
    # paginator = Paginator(cate, 15)
    # try:
    #     page_items = paginator.page(page)
    # except PageNotAnInteger:
    #     page_items = paginator.page(1)
    # except EmptyPage:
    #     page_items = paginator.page(paginator.num_pages)

    # contexts={ 'filter':category_filter, 'page_items':page_items, 'category':category }
    
   
    # if request.method == 'POST':

    #     name = request.POST.get('category')
    #     print('name',name)
    #     if Category.objects.filter(name=name).exists():
    #         messages.error(request,'Category name already exists!...')
    #         return redirect('category')
    #     Category.objects.create(name=name)
        
    #     return redirect('category')
    
    return render(request, 'home.html')



# # ----------------------------------- Category update -----------------------------------

# @require_http_methods(["POST"])
# def category_update(request, pk):

#     category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         try:
#             name = request.POST.get('name')            
#             category.name = name
#             category.save()

#             messages.success(request, 'Success! Category name updated successfully')
            
#         except Exception as e:
#             messages.error(request, 'Failed to update category name')
    
#     return redirect('category')

# # ----------------------------------- Category delete -----------------------------------


# def category_delete(request, pk):
#     try:
#         category = get_object_or_404(Category, pk=pk)
#         category.delete()
        
#         messages.success(request, f'Success! Category deleted successfully.')
        
#     except Exception as e:
#         messages.error(request, 'Category Delete failed')
#     return redirect('category')


# #--------------------------------------- category end------------------------