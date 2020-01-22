from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,template_name="main/index.html")

def userregister(request):
    if request.method == 'POST':
        formr = RegistrationForm(data=request.POST)
        if formr.is_valid():
            user=formr.save()
            user.set_password(user.password)
            user.save()
            username=formr.cleaned_data.get('username')
            password=formr.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('account:sucess')
    else:
        formr = RegistrationForm()
        return render(request, "main/userregister.html", {"formr":formr})


def userlogin(request):
    if request.method=='POST':
        usernam = request.POST['username']
        passwor = request.POST['password']
        user = auth.authenticate(request,username=usernam,password=passwor)
        if user is not None:
            auth.login(request,user)
            return redirect('account:sucess')
            
        else:
            return HttpResponse("Wrong CRedintials")
    
    else:
        return render(request, "main/userlogin.html")

            
def sucess(request):
    return render(request,"main/sucess.html",{"sucess":sucess})

