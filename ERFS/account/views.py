from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegistrationForm
from .profile import  profileForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.

def index(request):
    return render(request,template_name="index.html")

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
            
            return render(request, "main/userregister.html",{'error':"Given Username is Already Taken.Please Try Another."})
            
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
            return render(request, "main/userlogin.html",{'error':"Worng Username and Password"})
    else:
        return render(request, "main/userlogin.html")

def userlogout(request):
    logout(request)
    return render(request,"main/userlogout.html",{"userlogout":userlogout})

            
def sucess(request):
    return render(request,"main/sucess.html",{"sucess":sucess})


def uploadprofile(request):
    formp = profileForm()
    if request.method== "POST":
        formp = profileForm(request.FILES,request.POST)
        if formp.is_valid():
            formp.save()
        return redirect('account:viewprofile')
    return render(request, "main/profilecreation.html", {"formp":formp})

def viewprofile(request):
    userprofile= UserProfile.objects.all()
    return render(request, "main/profile.html",{"userprofile": userprofile})





