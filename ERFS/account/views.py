from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import RegistrationFormB
from .forms1 import RegistrationFormS
from .forms2 import LoginFormB
from .forms3 import LoginFormS
from endUser.models import Buyer,Seller

# Create your views here.

def index(request):
    return render(request,template_name="main/index.html")

def registerB(request):
    if request.method=="POST":
        form=RegistrationFormB(request.POST)
        if form.is_valid():
            form.save()
            username0=form.cleaned_data.get('registerB.username')
            password0=form.cleaned_data.get('registerB.password')
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
            username1=form1.cleaned_data.get('registerS.username')
            password1=form1.cleaned_data.get('registerS.password')
            seller= authenticate(username=username1,password=password1)
            login(request,seller)
            return redirect('account:upload')
    else:
        form1=RegistrationFormS()
    return  render(request,"main/registerS.html", {"form1":form1})

def loginB(request):
    if request.method=='POST':
        form2=LoginFormB(request.POST)
        
        buyer= authenticate(username=username,password=password)
        if buyer is not None:
            login(request,buyer)
            return render(request,"main/book.html")
        else:
            return render(request,"main/loginB.html",{'error':"Invalid Username and Password."})
    else:
        return render(request,"main/loginB.html",{"form2":form2})


def loginS(request):
    if request.method=='POST':
        form3=LoginFormS(request.POST)
        seller= authenticate(username=username,password=password)
        if seller is not None:
            login(request,seller)
            return render(request,"main/upload.html")
        else:
            return render(request,"main/loginS.html",{'error':"Invalid Username and Password."})
    else:
        return render(request,"main/loginS.html",{"form3":form3})


def book(request):
    return render(request,"main/book.html",{"book":book})

def upload(request):
    return render(request,"main/upload.html",{"upload":upload})