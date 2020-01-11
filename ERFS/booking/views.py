from django.shortcuts import render
from django.http import HttpResponse
from .models import Asset
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
def upload(request):
    if request.method=='POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request=request, template_name="uploads/upload.html", context={})


# Create your views here.
