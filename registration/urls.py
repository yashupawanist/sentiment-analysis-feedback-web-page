import os
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url 
from django.views.static import serve
from app1 import views

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('', include('web.urls')),
    url(r'^drug.jpg$', serve, {'document_root': os.path.join(BASE_DIR, 'static/images/'), 'path': 'drug.jpg'}),
]
