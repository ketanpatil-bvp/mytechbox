from django.urls import path, include
from . import views
from app import views as app_views

urlpatterns = [
    
    path('Login', app_views.UserLogin, name='Login'),
    path('Register', app_views.UserRegister, name='Register'),
    path('Logout', app_views.UserLogout, name='Logout'),
    
    
]
