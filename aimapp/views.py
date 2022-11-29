from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Gallery

def index(request):
    return render(request, 'index.html')

def gallery(request):
    dict_gallery = {
        "gallerys" : Gallery.objects.all(),
        }
    
    return render(request, 'base.html', dict_gallery)