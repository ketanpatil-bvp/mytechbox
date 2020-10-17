from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Post/<str:post_name>', views.ViewPost, name='Post'),
    path('Courses', views.Courses, name='Courses'),
    path('About', views.About, name='About'),

    
    
    
]
