from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request) :
    return render(request, 'projects.html')
def saybye(request):
    return render(request, 'project.html')