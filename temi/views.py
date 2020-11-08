from django.shortcuts import render,redirect,HttpResponse
from .models import *
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import *
from django.core.files.storage import FileSystemStorage
from .forms import *
def home(request):
    name = Name.objects.all()
    context = {
        'name': name
    }
    return render(request, 'temi/index.html', context)


def info(request, new_id):
    name = Name.objects.get(id= new_id)
    information = Information.objects.filter(name=name)
    context = {
        'information': information
    }
    return render(request, 'temi/info.html', context)


def sub_upload(request):
    if request.method == 'POST':
        form = Customername(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return redirect('')
    else:
        form = Customername()
    return render(request, 'temi/sub_upload.html', {'form': form})
    

def main_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return redirect('sub-upload')
    else:
        form = ImageForm()
        
    return render(request, 'temi/main_upload.html', {'form': form})
    

