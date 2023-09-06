from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings


#home page
def home(request):
    return HttpResponse("Welcome to home page.")



# def course(request):
#     return HttpResponse("Course")




# registeration page
def signup(request):   
    print("inside the signup")
    if request.method=='POST':
        form=SignupForm(request.POST, request.FILES)
        if form.is_valid():
            print("inside the signup form validtion")
            password = form.cleaned_data['password']
            hashed_password = make_password(password)
           
            user=form.save()
            user.password = hashed_password
            user.confirmation_token = uuid.uuid4()
            user.save()
            print(user)
             # Send a confirmation email
            confirmation_url = f"{settings.SITE_URL}/confirm/{user.confirmation_token}/"
            send_mail(
                'Confirm Your Email',
                f'Please click the following link to confirm your email: {confirmation_url}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            print(user)
            return HttpResponse("Please confirm your email.")
        
        return redirect('login')
        

    else:
        form=SignupForm()

    return render(request, 'app/signup.html', {'form':form})



def confirm_email(request, token):
    user = get_object_or_404(CustomUser, confirmation_token=token)
    
    # Mark the user's email as confirmed
    user.email_confirmed = True
    user.save()
    print(user.email_confirmed,"email confirmation code.")
    # Log in the user
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    
    return redirect('dashboard')



#dashboard page
def dashboard(request):
    return render(request, 'app/dashboard.html')


def instructor_dashboard(request):
    all_course=Course.objects.all()
    return render(request, 'app/instructor_dashboard.html', {'all_course':all_course})




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("inside form validation")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.email_confirmed:
                    login(request, user)

                    if user.role == 'student':
                        return redirect('dashboard')
                    else:
                        return redirect('instructor_dashboard')
                else:
                    return HttpResponse("Please confirm your email first.")
            else:
                return HttpResponse("Invalid username or password.")
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})







# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             print("inside form validation")
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user.email_confirmed:

#                 if user is not None:
#                     login(request, user)

#                     if user.role=='student':
#                         return redirect('dashboard')
#                     else:
#                         return redirect('instructor_dashboard')
                
#             else:
#                     return HttpResponse("please confirm your email first.")
#         else:
#             print(form.errors)
#     else:
#         form = AuthenticationForm()
#     return render(request, 'app/login.html', {'form': form})




def course(request):
    if request.method=='POST':
        form=CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('instructor_dashboard')
        else:
            print(form.errors)

    else:
        form=CourseForm()
     

    return render(request, 'app/course.html', {'form':form})



def update_course(request, pk):
    if pk:
        exist_course=get_object_or_404(Course, id=pk)
    else:
        exist_course=None

        print(exist_course)
    if request.method=='POST':
        form=CourseForm(request.POST, instance=exist_course)
        if form.is_valid():
            exist_course=form.save()
            return redirect('instructor_dashboard')
    else:
        form=CourseForm(instance=exist_course)


    return render(request, 'app/update_course.html', {'form':form})



def delete_course(request,pk):
    exist_course=get_object_or_404(Course, id=pk)
    if request.method=='POST':
        exist_course.delete()
        return redirect('instructor_dashboard')
    
    else:
        print("Not able to delete the course.")


    return HttpResponse("Course has been deleted for giving particular id.")