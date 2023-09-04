from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import *

#home page
def home(request):
    return HttpResponse("Welcome to home page.")


#registeration page
def signup(request):   
    print("inside the signup")
    if request.method=='POST':
        form=SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            print(user)
            return redirect('login')

    else:
        form=SignupForm()

    return render(request, 'app/signup.html', {'form':form})
    

#dashboard page
def dashboard(request):
    return render(request, 'app/dashboard.html')


#login page
def login(request):
    print("inside the login page")
    if request.method=='POST':
        print("post")
        print("form validation")
        username =request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
                    login(request, user)
                    return redirect('dashboard')
            
        else:
             print("Wrong credentials.")

    return render(request, 'app/login.html')
    

   

