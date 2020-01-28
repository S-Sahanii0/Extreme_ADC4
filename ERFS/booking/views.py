from django.shortcuts import render,redirect, get_object_or_404
from .models import Asset, Booking, AddToFav
from .forms import UploadForm
from django.http import HttpResponse
from django.contrib import messages


def upload(request):
    form= UploadForm()
    if request.method == "POST":
        form= UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('booking:display')       
    return render(request, "uploads/upload.html", {"form": form})

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

def delete_asset(request, pk= None):
    asset= Asset.objects.get(pk=pk)
    asset.delete()
    return redirect('booking:display')

def fav_list(request,id):
    #is_favorite = False
    #if asset.favorite.filter(id=request.user.id).exists():
        #is_favorite = True
    #context = {
        #"is_favorite":is_favorite
    #}
    #asset = get_object_or_404(Asset, id=id)
    #if asset.favorite.filter(id= request.user.id).exists():
        #asset.favorite.remove(request.user)
    #else:
        #asset.favourite.add(request.user)
    #return redirect(asset.get_absolute_url())"""
    asset = get_object_or_404(Asset, id=id)
    if asset.is_favorite:
        asset.is_favorite = False
        asset.save()
        messages.info(request, 'You have marked asset {} as favorite!'.format(asset.asset_id))
    else:
        asset.is_favorite = True
        asset.save()
        messages.info(request, 'You have removed asset {} from favorite'.format(asset.asset_id))

def book_asset(request,pk):
    asset = get_object_or_404(Asset, pk=pk)
    if asset.is_available:
        asset.is_available= False
        asset.save()
        messages.info(request, 'You have marked asset {} as booked!'.format(asset.asset_id))
    else:
        asset.is_available = True
        asset.save()
        messages.info(request, 'You have marked asset {} as available for booking'.format(asset.asset_id) )
    return redirect('booking:display')