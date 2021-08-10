from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request, pk) :
    return HttpResponse('Hello there !!!' + ' ' + str(pk))
def saybye(request):
    return HttpResponse('See you. Have a nice day.')