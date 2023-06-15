
from django.shortcuts import render, redirect
from .models import MainService
from django.http import HttpRequest
import datetime
# Create your views here.


def service(request: HttpRequest):
    """Rendering the service page to show all the services that are available in the database"""

    services = MainService.objects.all()

    if services:
        return render(request, 'main_app/services.html', {'services': services})
    else:
        return render(request, 'service_app/add_service.html')




def add_service(request:HttpRequest):
    """"Add a new service to the database and redirect to the service page"""
    if request.method == 'POST':
        new_service = MainService(name_service=request.POST["name_service"], description_service=request.POST["description_service"])
        new_service.save()
        return redirect('service_app:service')

    return render(request,'service_app/add_service.html')