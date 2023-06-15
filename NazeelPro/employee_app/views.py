
from django.http import HttpRequest
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from guest_app.models import Guest, Stay
from employee_app.models import Employee

# Create your views here.


def employee(request: HttpRequest):
    """rendering employee template """

    return render(request, 'employee_app/employee.html')



def add_guest(request: HttpRequest):
    """rendering add guest template """
    if request.method == 'POST':
        # user = User.objects.create_user(
        #     username=request.POST["guest_room_number"], password=request.POST["guest_phone_number"], first_name=request.POST["guest_name"])
        # user.save()
        # get the User instance
        user = request.user

        # get the Employee instance linked to the User
        employee = Employee.objects.get(user=user)

        # create the Guest instance
        guest = Guest.objects.create(
            created_by=employee,
            name=request.POST["guest_name"],
            room_number=request.POST["guest_room_number"],
            phone_number=request.POST["guest_phone_number"]
        )

        return render(request, 'employee_app/add_guest.html')

        # stay = Stay(
        #     user=user, check_in_date=request.POST["check_in_date"], check_out_date=request.POST["check_out_date"])
        # stay.save()

    return render(request, 'employee_app/add_guest.html')
