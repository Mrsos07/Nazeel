from django.shortcuts import render, redirect
from .models import MainService
from django.http import HttpRequest
# Create your views here.


def service(request:HttpRequest):
    services = MainService.objects.all()

    return render(request,'main_app/services.html', {'services': services})

def add_service(request:HttpRequest):
    if request.method == 'POST':
        new_service = MainService(name_service=request.POST["name_service"], description_service=request.POST["description_service"])
        new_service.save()
        return redirect('service_app:service')

    return render(request,'service_app/add_service.html')