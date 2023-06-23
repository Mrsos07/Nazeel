from datetime import datetime
from django.shortcuts import render, redirect
from .models import MainService, SubService, Review , Room , SubServiceRequest
from main_app.models import Hotel
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.urls import reverse


# Create your views here.
from guest_app.models import Guest


def service(request: HttpRequest):
    """Rendering the service page to show all the services that are available in the database"""

    services = MainService.objects.all()
    reviews = Review.objects.all()
    return render(request, 'main_app/services.html', {'services': services, 'reviews': reviews})

@permission_required('service_app.add_mainservice', raise_exception=True)
def manager_services(request: HttpRequest):
    main_services = MainService.objects.all()
    return render(request, "service_app/manager_services.html", {'main_services': main_services})

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
                name_service=request.POST["name_service"], description_service=request.POST["description_service"],
                time_on=time__on, time_off=time__off, image=request.FILES["image"], hotel=hotel)
        else:
            new_service = MainService(
                name_service=request.POST["name_service"], description_service=request.POST["description_service"],
                time_on=time__on, time_off=time__off, hotel=hotel)
        new_service.save()
        return redirect('service_app:manager_services')

    return render(request, 'service_app/add_service.html', {'hotels': hotels})


def submit_request(request: HttpRequest):

    sub_service = SubService.objects.get(id=request.POST["sub_services_id"])
    room = Room.objects.get(id=request.POST["room_id"])
    new_request = SubServiceRequest(
        sub_service=sub_service, room=room, quantity=request.POST["quantity"])
    new_request.save()

    return redirect("main_app:history")

def update_request(request: HttpRequest, request_id):
    new_request = SubServiceRequest.objects.get(id=request_id)
    new_request.is_delivered = request.POST["is_delivered"]
    new_request.save()

    return redirect(reverse("service_app:active_order", kwargs={'main_services_id': new_request.sub_service.main_service.id}))

def edit_main_service(request: HttpRequest, main_services_id):
    main_services = MainService.objects.get(id = main_services_id)
    #hotel = Hotel.objects.get(id=request.POST['hotel'])
    # Get the user input for the `time_on` field
    if request.method == 'POST':
        time_on = request.POST['time_on']
        time_off = request.POST['time_off']

        # Convert the input string to a datetime object
        time__on = datetime.strptime(time_on,  '%H:%M')
        time__off = datetime.strptime(time_off,  '%H:%M')  
        main_services.name_service = request.POST["name_service"]
        main_services.description_service = request.POST["description_service"]
        main_services.time_on = time__on
        main_services.time_off = time__off
        # main_services.hotel=hotel 
        if "image" in request.FILES:
            main_services.image = request.FILES["image"]
        main_services.save()
        return redirect('service_app:manager_services')
    return render(request, "service_app/edit_main_service.html",{"main_services":main_services})

def delete_service(request:HttpRequest, main_services_id):
    main_services = MainService.objects.get(id=main_services_id)
    main_services.delete()
    return redirect('service_app:manager_services')

@permission_required('service_app.add_mainservice', raise_exception=True)
def menu(request:HttpRequest, main_services_id):
    main_services = MainService.objects.get( id = main_services_id )
    sub_service = SubService.objects.filter(main_service=main_services)
    return render(request, "service_app/menu.html", {'main_services': main_services, 'sub_service': sub_service})

@permission_required('service_app.edit_items', raise_exception=True)
def edit_items(request: HttpRequest, main_services_id):
    if request.method == 'POST':
        main_services_object = MainService.objects.get(id=main_services_id)

        new_sub_service = SubService(main_service=main_services_object, name_service=request.POST["name_service"], catogory=request.POST[
                                     "catogory"], price=request.POST["price"], image=request.FILES["image"])
        new_sub_service.save()
        return redirect("service_app:edit_items", main_services_id=main_services_id)
    main_services = MainService.objects.get(id=main_services_id)
    delete_items = SubService.objects.filter(main_service=main_services_id)
    return render(request, "service_app/edit_items.html", {"delete_items": delete_items, "main_services": main_services})






@permission_required('service_app.delete_mainservice', raise_exception=True)
def delete_items(request: HttpRequest, item_id):
    deleted_items = SubService.objects.get(id=item_id)

    main_services_id = MainService.objects.get(id=deleted_items.main_service.id)

    deleted_items.delete()
    return redirect('service_app:edit_items', main_services_id=main_services_id.id)


def order_request(request: HttpRequest, main_services_id):
    main_services = MainService.objects.get(id=main_services_id)
    sub_service = SubService.objects.filter(main_service=main_services)

    return render(request, "service_app/order_request.html", {'main_services': main_services, 'sub_service': sub_service})

#def is_deliverd(request:HttpRequest):
    #deliverd=SubService.objects.filter(id=order_id)
 #   sub_request=SubServiceRequest.objects.filter(is_deliverd)
  #  if sub_request.is_deliverd ==True:
   #     sub_request.is_deliverd=False
    #else:
     #   sub_request.is_deliverd=True

    #return render(request, "service_app/active_order.html",)




def active_order(request: HttpRequest, main_services_id):
    main_services = get_object_or_404(MainService, id=main_services_id)

    is_delivered_status= SubServiceRequest.objects.all()

    user_requests = SubServiceRequest.objects.filter(sub_service__main_service=main_services)

    if request.method == 'POST':
        is_delivered = request.POST['is_delivered']

    return render(request, 'service_app/active_order.html', {"user_requests": user_requests})

def edit_main_service(request: HttpRequest, main_services_id):
    main_services = MainService.objects.get(id = main_services_id)
    #hotel = Hotel.objects.get(id=request.POST['hotel'])
    # Get the user input for the `time_on` field
    if request.method == 'POST':
        time_on = request.POST['time_on']
        time_off = request.POST['time_off']

        # Convert the input string to a datetime object
        time__on = datetime.strptime(time_on,  '%H:%M')
        time__off = datetime.strptime(time_off,  '%H:%M')
        main_services.name_service = request.POST["name_service"]
        main_services.description_service = request.POST["description_service"]
        main_services.time_on = time__on
        main_services.time_off = time__off
        # main_services.hotel=hotel
        if "image" in request.FILES:
            main_services.image = request.FILES["image"]
        main_services.save()
        return redirect('service_app:manager_services')
    return render(request, "service_app/edit_main_service.html",{"main_services":main_services})

def delete_service(request:HttpRequest, main_services_id):
    main_services = MainService.objects.get(id=main_services_id)
    main_services.delete()
    return redirect('service_app:manager_services')