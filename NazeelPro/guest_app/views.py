from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from guest_app.models import Guest


# Create your views here.


def sign_in(request: HttpRequest,):
    """rendering sign in template"""
    msg = None
    if request.method == "POST":
        # user: User = authenticate(
        #     request, username=request.POST["room_number"], password=request.POST["phone_number"])
        guest = Guest.objects.all()
        if guest is not None:
            return redirect("main_app:home")

    return render(request, "guest_app/sign_in.html")


def guest_home(request: HttpRequest):
    """rendering sign in template"""

    return render(request, 'guest_app/guest_home.html')
