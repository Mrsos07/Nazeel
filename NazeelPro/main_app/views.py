from django.shortcuts import render
from django.http import HttpRequest
from service_app.models import MainService , SubService

# Create your views here.

def home(request:HttpRequest):
    """Rendering the home page template"""
    services = MainService.objects.all()[:3]
    return render(request,'main_app/home.html',{"services":services})

def history(request:HttpRequest):
    return render(request,'main_app/history.html')

def services(request:HttpRequest):
    return render(request,'main_app/services.html')

def about(request:HttpRequest):
    return render(request,'main_app/about.html')

def order(request:HttpRequest,main_services_id):
    main_services = MainService.objects.get( id = main_services_id )
    sub_service = SubService.objects.filter(main_service=main_services)
    return render(request,'main_app/order.html',{'main_services': main_services,'sub_service': sub_service})

def maps(request:HttpRequest):
    return render(request,'main_app/maps.html')