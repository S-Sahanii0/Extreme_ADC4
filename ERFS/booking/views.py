from django.shortcuts import render,redirect, get_object_or_404
from .models import Asset
from .forms import UploadForm


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

#def fav_list(request,id):
    #asset = get_object_or_404(Asset, id=id)
    #if request.method == 'POST':
        #asset.favourite.add(request.user)
    #return render(request, "uploads/details.html", {"assets": asset})
# Create your views here.
