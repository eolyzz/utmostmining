from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name= 'contact'),
    path('payment/',views.payment, name = 'payment'),
    path('forgot-password/',views.forgot_password, name = 'forgot-password'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    
] + static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
