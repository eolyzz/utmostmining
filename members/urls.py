from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup_user/',views.signup_user, name = 'signup'),
    path('login_user/',views.login_user, name = 'login'),
    path("logout_user/",views.logout_user, name = 'logout'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    
]
handler404 = "members.views.handle_not_found"