from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,template_name="main/index.html")

def userregister(request):
    if request.method == 'POST':
        formr = RegistrationForm(data=request.POST)
        if formr.is_valid():
            user = formr.save()
            user.save()
    else:
        formr = RegistrationForm()


def userlogin(request):
    pass




def sucess(request):
    return render(request,"main/sucess.html",{"sucess":sucess})

