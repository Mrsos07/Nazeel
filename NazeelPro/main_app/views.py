from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home(request:HttpRequest):
    """Rendering the home page template"""
    return render(request,'main_app/home.html')

def history(request:HttpRequest):
    return render(request,'main_app/history.html')