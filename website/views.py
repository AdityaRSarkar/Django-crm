from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,Add_customer_form
from .models import Customer
def home(request):
    customers=Customer.objects.all()
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
    return render(request, 'home.html',{'customers':customers})

def logout_user(request):
    logout(request)
    messages.success(request,"Logout Successful!")
    return redirect('home') 

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login the user after successful registration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered!")
                return redirect('home')
            else:
                messages.error(request, "There was a problem logging you in. Please try again.")
        else:
            messages.error(request, "There was an error with your submission. Please correct the errors below.")
    else:
        form = SignUpForm()  

    # In case of GET request or invalid POST data, render the registration form again
    return render(request, 'register.html', {'form': form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        return render(request, 'Record.html', {'customer_record': customer_record})
    else:
        messages.error(request,"You must be logged in to view the customer records")
    
    return redirect('home')

def Delete_customer(request,pk):
    if request.user.is_authenticated:
        delete_it=Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,f"The Customer Record for {delete_it.first_name} {delete_it.last_name} has been deleted")
        return redirect('home')
    else:
        messages.error(request,"You have to login first to delete Customer Records")
    return redirect('home')

def Add_customer(request):
    form=Add_customer_form(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_customer=form.save()
                messages.success(request,"Customer Added Successfully")
                return redirect('home')    
        return render(request, 'Add.html', {'form':form})
    messages.error(request,"You must be logged in to add")
    return redirect('home')
    
def Update_customer(request,pk):
    if request.user.is_authenticated:
        current_record=Customer.objects.get(id=pk)
        form=Add_customer_form(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been Updated!")
            return redirect('home')
        return render(request, 'Update.html', {'form':form,'current_record':current_record})
    messages.error(request,"You must be logged in to add")
    return redirect('home')   
