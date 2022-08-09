from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/',views.about, name = 'about'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('payment/',views.payment, name = 'payment'),
    path('signIn/',views.signIn, name = 'signIn'),
    path('signUp/',views.signUp, name = 'signUp'),
]
