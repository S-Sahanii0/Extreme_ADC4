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
        form2=LoginFormB()
        username2 =request.POST['username']
        password2 =request.POST['password']
        buyer= authenticate(username=username2,confirm_password=password2)
        if buyer is None:
            return render(request,"main/loginB.html",{'error':"Invalid Username and Password."})
        else:
            login(request,buyer)
            return redirect('account:book')
            
    else:
        form2=LoginFormB()
        return render(request,"main/loginB.html",{"form2":form2})


def loginS(request):
    if request.method=='POST':
        form3=LoginFormS()
        username3=request.POST['username']
        password3 =request.POST['password']
        seller= authenticate(username=username3,confirm_password=password3)
        if seller is None:
            return render(request,"main/loginS.html",{'error':"Invalid Username and Password."})
        else:
            login(request,seller)
            return redirect('account:upload')
            
    else:
        form3=LoginFormS()
        return render(request,"main/loginS.html",{"form3":form3})



def book(request):
    return render(request,"main/book.html",{"book":book})


def upload(request):
    return render(request,"main/upload.html",{"upload":upload})