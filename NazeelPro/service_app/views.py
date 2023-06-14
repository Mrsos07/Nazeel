from django.shortcuts import render, redirect
from django.http import HttpRequest
# Create your views here.


def service(request:HttpRequest):

    return render(request,'main_app/services.html')

def add_service(request:HttpRequest):
    if request.method == 'POST':
        return redirect('service_app:service')

    return render(request,'service_app/add_service.html')