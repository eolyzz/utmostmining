from django.shortcuts import render 

def homepage (request):
    return render (request, 'homepage.html', {})

def about (request):
    return render (request, 'about.html', {})

def dashboard (request):
    return render (request, 'dashboard.html', {})

def payment (request):
    return render (request, 'payment.html', {})

def signIn (request):
    return render (request, 'signIn.html', {})

def signUp (request):
    return render (request, 'signUp.html', {})