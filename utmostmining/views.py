from django.shortcuts import render, redirect


def homepage (request):
    return render (request, 'homepage.html', {})

def contact (request):
    return render (request, 'contact.html', {})

def about (request):
    return render (request, 'about.html', {})

def payment (request):
    return render (request, 'payment.html', {})

def forgot_password (request):
    return render (request, 'forgot-password.html', {})

def handle_not_found (request, exception):
    return redirect('homepage')