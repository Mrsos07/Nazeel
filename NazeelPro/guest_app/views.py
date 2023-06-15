from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def sign_in(request:HttpRequest):
    """rendering sign in template"""
    msg = None
    if request.method == "POST":
        user : User = authenticate(request, room_number=request.POST["room_number"], phone_number=request.POST["phone_number"])
        if user:
            login(request, user)
            return redirect("main_app:home")
        else:
            msg = "Incorrect Credentials"

    return render(request,'guest_app/sign_in.html', {"msg" : msg})


def guest_home(request:HttpRequest):
    """rendering sign in template"""

    return render(request,'guest_app/guest_home.html')
