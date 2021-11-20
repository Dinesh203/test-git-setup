from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm , UserCreationForm, BlogForm
# from .models import Blogs

def home(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "user has been registered")
            form = SignUpForm()
            return render(request, 'signup.html', {'form': form})

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "user has been registered")
#             form = UserCreationForm()
#             return render(request, 'signup.html', {'form': form})

#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            authuser = authenticate(username=uname, password=upass)
            login(request, authuser)
            messages.success(request, "user Login successfully!!")
            return render(request, 'user_profile.html')
    else:
        fm = AuthenticationForm()
    return render(request, "login.html", {'form':fm})


def profile(request):
    print(BlogForm)
    if request.method == 'POST':
        blog = BlogForm(request.POST)
        if blog.is_valid():
            blog.save()
            messages.success(request, "blog has been created")
            blog = BlogForm()
            return render(request, 'user_profile.html', {'blg': blog})

    else:
        blog = BlogForm()
        return render(request, 'user_profile.html', {'blg':blog})



def user_logout(request):
    logout(request)
    return render(request, "signup.html")

