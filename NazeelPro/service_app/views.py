from datetime import datetime

from django.shortcuts import render, redirect
from .models import MainService , SubService
from main_app.models import Hotel
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def service(request: HttpRequest):
    """Rendering the service page to show all the services that are available in the database"""

    services = MainService.objects.all()
    if services:
        return render(request, 'main_app/services.html', {'services': services})
    else:
        return render(request, 'service_app/add_service.html')

@permission_required('service_app.add_mainservice', raise_exception=True)
def manager_services(request:HttpRequest):
    main_services = MainService.objects.all()
    return render(request, "service_app/manager_services.html",{'main_services': main_services})


@permission_required('service_app.add_mainservice', raise_exception=True)
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
        return redirect('service_app:manager_services')

    return render(request, 'service_app/add_service.html', {'hotels': hotels})

@permission_required('service_app.add_mainservice', raise_exception=True)
def menu(request:HttpRequest, main_services_id):
    main_services = MainService.objects.get( id = main_services_id )
    sub_service = SubService.objects.filter(main_service=main_services)
    
    return render(request,"service_app/menu.html",{'main_services': main_services,'sub_service': sub_service})

@permission_required('service_app.change_subservice', raise_exception=True)
def edit_items(request:HttpRequest,main_services_id):
    if request.method == 'POST':
        main_services_object = MainService.objects.get(id = main_services_id)
        new_sub_service = SubService(main_service=main_services_object,name_service=request.POST["name_service"],catogory=request.POST["catogory"],price=request.POST["price"],image=request.FILES["image"],delivery_time=request.POST["delivery_time"])
        new_sub_service.save()
        return redirect("service_app:edit_items",main_services_id=main_services_id)
    
    main_services=MainService.objects.get( id = main_services_id )
    delete_items=SubService.objects.filter(main_service=main_services_id)
    return render(request,"service_app/edit_items.html",{"delete_items":delete_items,"main_services":main_services})

@permission_required('service_app.delete_mainservice', raise_exception=True)
def delete_items(request:HttpRequest,item_id):
    deleted_items=SubService.objects.get(id=item_id)
    main_services_id=MainService.objects.get(id=deleted_items.main_service.id)
    deleted_items.delete()
    return redirect('service_app:edit_items', main_services_id=main_services_id.id)

def order_request(request:HttpRequest, main_services_id):
    main_services = MainService.objects.get( id = main_services_id )
    sub_service = SubService.objects.filter(main_service=main_services)
    return render(request,"service_app/order_request.html",{'main_services': main_services,'sub_service': sub_service})

def active_order(request:HttpRequest, main_services_id):
    main_services = MainService.objects.get( id = main_services_id )
    sub_service = SubService.objects.filter(main_service=main_services)
    return render(request,"service_app/active_order.html",{'main_services': main_services,'sub_service': sub_service})