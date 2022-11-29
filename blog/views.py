from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Post

def blog(request):
    posts = {
        'post': Post.objects.all()
    }
    return render(request, 'blog.html',posts)