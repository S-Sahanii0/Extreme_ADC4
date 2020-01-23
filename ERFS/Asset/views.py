from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Asset
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, "home.html",)

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match = Asset.objects.filter(Q(asset_Title__startswith=srch) | Q(asset_Title__icontains=srch))

            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else: 
            return HttpResponseRedirect('/search/')         
    return render(request,'search.html')  