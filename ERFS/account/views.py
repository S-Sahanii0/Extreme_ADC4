from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationFormB
from endUser.models import Buyer,Seller

# Create your views here.

def index(request):
    return render(request,template_name="main/index.html")

def registerB(request):
    if request.method=="POST":
        form=RegistrationFormB(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:index')
    else:
        form=RegistrationFormB()
    return  render(request,"main/register.html", {"form":form})


def registerS(request):
    if request.method=="POST":
        form=RegistrationFormS(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:index')
    else:
        form=RegistrationFormS()
    return  render(request,"main/register.html", {"form":form})
def login(request):
    return HttpResponse("hello login")

def logout(request):
    return HttpResponse("hello logout")
