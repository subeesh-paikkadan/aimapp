from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Exam

def exam(request):
    results = Exam.objects.all()
    return render(request, 'exam.html', {"Exam": results})