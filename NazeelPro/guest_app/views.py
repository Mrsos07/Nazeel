from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def sign_in(request:HttpRequest):
    """rendering sign in template"""

    return render(request,'guest_app/sign_in.html')


def guest_home(request:HttpRequest):
    """rendering sign in template"""

    return render(request,'guest_app/guest_home.html')