from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about_me(request):
    return HttpResponse("Hello, this would be the about page")