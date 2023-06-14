from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def sign_in(request:HttpRequest):

    return render(request,'guest_app/sign_in.html')