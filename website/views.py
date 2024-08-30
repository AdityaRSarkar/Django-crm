from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        # Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.error(request, "Login failed. Please try again.")
    
# Ensure the view always returns a response, even for GET requests
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(request,"Logout Successful!")
    return redirect('home') 

def register_user(request):
     return render(request, 'register.html')