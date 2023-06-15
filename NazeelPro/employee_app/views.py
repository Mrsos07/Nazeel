from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect
# Create your views here.

def employee(request:HttpRequest):
    """rendering employee template """

    return render(request,'employee_app/employee.html')


def add_guest(request:HttpRequest):

    return render(request,'employee_app/add_guest.html')