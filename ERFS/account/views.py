from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from endUser.models import EndUser
from django import forms
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,template_name="main/index.html")

def register(request):
        if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        return redirect('/')
    else:
        return render(request,'user/register.html',context={})

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            buyer= authenticate(username=username,password=password)
            login(request,buyer)
            return redirect('account:book')
    else:
        form=RegistrationForm()
    return  render(request,"main/register.html", {"form":form})


def login(request):
    pass




def sucess(request):
    return render(request,"main/sucess.html",{"sucess":sucess})

