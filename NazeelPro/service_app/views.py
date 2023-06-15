from datetime import datetime

from django.shortcuts import render, redirect
from .models import MainService
from main_app.models import Hotel
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





def add_service(request: HttpRequest):
    """"Add a new service to the database and redirect to the service page"""
    hotels = Hotel.objects.all()
    if request.method == 'POST':
        hotel = Hotel.objects.get(id=request.POST['hotel'])
        # Get the user input for the `time_on` field
        time_on = request.POST['time_on']
        time_off = request.POST['time_off']

        # Convert the input string to a datetime object
        time__on = datetime.strptime(time_on,  '%H:%M')
        time__off = datetime.strptime(time_off,  '%H:%M')
        if "image" in request.FILES:

            new_service = MainService(
                name_service=request.POST["name_service"], description_service=request.POST["description_service"], time_on=time__on, time_off=time__off, image=request.FILES["image"], hotel=hotel)
        else:
            new_service = MainService(
                name_service=request.POST["name_service"], description_service=request.POST["description_service"], time_on=time__on, time_off=time__off, hotel=hotel)
        new_service.save()
        return redirect('service_app:service')

    return render(request, 'service_app/add_service.html', {'hotels': hotels})
