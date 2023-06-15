from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect
# Create your views here.

def employee(request:HttpRequest):
    """rendering employee template """

    return render(request,'employee_app/employee.html')



