from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name= 'contact'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('payment/',views.payment, name = 'payment'),
    path('login/',views.login, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('forgot-password/',views.forgot_password, name = 'forgot-password'),
    
] + static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
