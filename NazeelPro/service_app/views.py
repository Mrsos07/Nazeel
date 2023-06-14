from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def service(request:HttpRequest):

    return render(request,'service_app/service.html')