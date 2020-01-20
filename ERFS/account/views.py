from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegistrationFormB
from .forms1 import RegistrationFormS
from django.contrib.auth.forms import AuthenticationForm
from endUser.models import Buyer,Seller
from django import forms
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,template_name="main/index.html")

def registerB(request):
    if request.method=="POST":
        form=RegistrationFormB(request.POST)
        if form.is_valid():
            form.save()
            username0=form.cleaned_data.get('username')
            password0=form.cleaned_data.get('password')
            buyer= authenticate(username=username0,password=password0)
            login(request,buyer)
            return redirect('account:book')
    else:
        form=RegistrationFormB()
    return  render(request,"main/registerB.html", {"form":form})


def registerS(request):
    if request.method=="POST":
        form1=RegistrationFormS(request.POST)
        if form1.is_valid():
            form1.save()
            username1=form1.cleaned_data.get('username')
            password1=form1.cleaned_data.get('password')
            seller= authenticate(username=username1,password=password1)
            login(request,seller)
            return redirect('account:upload')
    else:
        form1=RegistrationFormS()
    return  render(request,"main/registerS.html", {"form1":form1})

def loginB(request):
    if request.method=='POST':
        f2=AuthenticationForm(request=request,data=request.POST)
        if f2.is_valid():
            username2=f2.cleaned_data.get('username')
            password2=f2.cleaned_data.get('password')
            buyer= authenticate(request,username=username2,password=password2)
            if buyer is not None:
                    login(request,buyer)
                    return redirect('account:book')
                
        else:
            return render(request,"main/loginB.html",{'error':"Invalid Username and Password."})
            
    else:
        f2=AuthenticationForm()
        return render(request,"main/loginB.html",{"f2":f2})


def loginS(request):
    if request.method=='POST':
        f3=AuthenticationForm(request.POST)
        username3=f3.cleaned_data['username']
        password3 =f3.cleaned_data['password']
        seller= authenticate(username=username3,confirm_password=password3)
        if seller is None:
            return render(request,"main/loginS.html",{'error':"Invalid Username and Password."})
        else:
            login(request,seller)
            return redirect('account:upload')
            
    else:
        f3=AuthenticationForm()
        return render(request,"main/loginS.html",{"f3":f3})



def book(request):
    return render(request,"main/book.html",{"book":book})


def upload(request):
    return render(request,"main/upload.html",{"upload":upload})