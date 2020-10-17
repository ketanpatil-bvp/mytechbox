from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .forms import UserRegistrationForm, UserLoginForm
from random import randint

# Create your views here.
def Home(request):
    posts = Post.objects.all()
    return render(request, 'app/index.html',{'posts':posts})

def ViewPost(request, post_name):
    post = Post.objects.get(post_name=post_name)
    return render(request,'app/post.html',{'post':post})

def Courses(request):
    return render(request, 'app/courses.html')
 
def About(request):
    return render(request, 'app/about.html')

def UserRegister(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)   
            user.username = f"{(form.cleaned_data['email']).split('@')[0]}{randint(5000,6000)}"
            user.save()
            return redirect('Login')
    else:
        form = UserRegistrationForm()
    return render(request,'app/signup.html',{'form':form})


def UserLogin(request):
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')

            
    
    else:
        form = UserLoginForm()
        

    return render(request,'app/login.html',{"form":form})

def UserLogout(request):
    logout(request)
    return redirect('Home')

