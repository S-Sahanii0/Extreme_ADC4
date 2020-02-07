from django.shortcuts import render,redirect, get_object_or_404
from .models import Asset,Booking
from account.models import UserProfile
from .forms import UploadForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='account:userlogin')
def upload(request):
    #form= UploadForm()
    if request.method == "POST":
        form= UploadForm(request.POST, request.FILES)
        if form.is_valid():
            asset=form.save(commit=False)
            asset.user=request.user
            asset.save()
        return redirect('booking:display') 
    else:      
        form= UploadForm()
        return render(request, "uploads/uploads.html", {"form": form})
@login_required(login_url='account:userlogin')
def update_asset(request, id=None):
    instance= get_object_or_404(Asset, id=id)
    form= UploadForm()
    if request.method == "POST":
        form= UploadForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('booking:display')       
    return render(request, "uploads/upload.html", {"form": form})

def display(request):
    asset= Asset.objects.all()
    return render(request, "uploads/details.html",{"assets": asset})

@login_required(login_url='account:userlogin')
def delete_asset(request, pk= None):
    asset= Asset.objects.get(pk=pk)
    asset.delete()
    return redirect('booking:display')

@login_required(login_url='account:userlogin')

def book_asset(request,pk=None):
    asset = get_object_or_404(Asset, pk=pk)
    if asset.is_available:
        asset.is_available= False
        asset.save()
        b=Booking(user_id=request.user.id)
        b.booking_Date=timezone.now()
        b.asset_id=pk
        b.booking_Status=True
        b.save()
        return redirect('booking:display')

        #messages.info(request, 'You have marked asset {} as booked!'.format(asset.asset_id))
    else:
        asset.is_available = True
        asset.save()
        #messages.info(request, 'You have marked asset {} as available for booking'.format(asset.asset_id) )

    