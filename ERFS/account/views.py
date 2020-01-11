from django.shortcuts import render
from django.http import HttpResponse
from endUser.models import Buyer,Seller

# Create your views here.

def index(request):
    return render(request,template_name="main/index.html")

def register(request):
        return  render(request,template_name="main/register.html")

def login(request):
    return HttpResponse("hello login")

def logout(request):
    return HttpResponse("hello logout")
