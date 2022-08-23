from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

# Create your views here.
def signup_user (request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("first_name")
            messages.success(request, f"Hello {user}, Sign was successful")
        
            return redirect ('login')
    else:
        form = CreateUserForm()
    context = {
                'form':form
                }
    return render (request, 'authenticate/register.html', context)
            
 
def login_user (request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')   
    else:
        form = CreateUserForm()
    context = {
                'form':form
                }
    return render (request, 'authenticate/login.html', context)


def logout_user (request):
        logout (request)
        return redirect("login")

@login_required(login_url="login")
def dashboard (request):
    return render (request, 'dashboard.html')