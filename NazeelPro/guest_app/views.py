from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from guest_app.models import Guest , Room


# Create your views here.


def sign_in(request: HttpRequest,):
    """Rendering sign in template"""
    if request.method == "POST":
        # retrieve the inputs
        room_number = request.POST["room_number"]
        phone_number = request.POST["phone_number"]


        # check if a Room with this room_number exists
        try:
            room = Room.objects.get(room_number=room_number)
        except Room.DoesNotExist:
            messages.error(request, "Incorrect room number")
            return render(request, "guest_app/sign_in.html")

        # check if a Guest with this room and phone_number exists
        try:
            guest = Guest.objects.get(room=room, phone_number=phone_number)
            user, created = User.objects.get_or_create(username=guest.name, defaults={'password': 'Mm112233'})
            user.save()
            if guest and user.is_authenticated:
                login(request,user)
            # guest found, redirect to home
                return redirect("main_app:home")
        except Guest.DoesNotExist:    # guest not found, send error message and show the sign_in page again
            messages.error(request, "Incorrect phone number")

    # if request.method is not POST or if login failed
    return render(request, "guest_app/sign_in.html")


def guest_home(request: HttpRequest):
    """rendering sign in template"""

    return render(request, 'guest_app/guest_home.html')
