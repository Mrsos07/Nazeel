
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from guest_app.models import Guest, Stay, Room
from employee_app.models import Employee
from main_app.models import Hotel

# Create your views here.


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def employee(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # المصادقة على بيانات تسجيل الدخول المدخلة
        user = authenticate(request, username=username, password=password)

        if user is not None and user.employee is not None:
            # تم العثور على مستخدم موظف صحيح، قم بتسجيل دخوله
            login(request, user)
            return redirect('service_app:manager_services')  # توجيه الموظف إلى صفحة البداية الخاصة به

        else:
            # بيانات تسجيل الدخول غير صحيحة، قم بعرض رسالة خطأ
            error_message = 'Invalid username or password'
            return render(request, 'employee_app/employee.html', {'error_message': error_message})

    else:
        # إذا كان الطلب غير POST، قم بعرض صفحة تسجيل الدخول
        return render(request, 'employee_app/employee.html')


@login_required
@permission_required('guest_app.add_guest', raise_exception=True)
def add_guest(request: HttpRequest,):
    if request.method == 'POST' and request.user.is_authenticated:
        # get the Employee instance linked to the User
        employee = Employee.objects.get(user=request.user)

        # get the room number from the POST data and use it to get the Room instance
        room_number = request.POST["guest_room_number"]
        room = Room.objects.get(room_number=room_number)

        # create the Guest instance with the Room
        guest = Guest.objects.create(
            created_by=employee,
            name=request.POST["guest_name"],
            room=room,
            phone_number=request.POST["guest_phone_number"]
        )

        # set the room as not available anymore
        room.is_available = False
        room.save()

        return redirect('main_app:home')
    else:
        # get all available rooms
        available_rooms = Room.objects.filter(is_available=True)

        return render(request, 'employee_app/add_guest.html', {'available_rooms': available_rooms})


def add_room(request: HttpRequest):
    all_hotels = Hotel.objects.all()
    # if request.method == 'POST' :
    #     hotel_object = Hotel.objects.get(id=hotel_id)
    #     new_room = Room(hotel=hotel_object,room_number=request.POST["room_number"])
    #     new_room.save()
    #     return redirect('employee_app:manager_services',hotel_id=hotel_id)
    # hotel = Hotel.objects.get(id=hotel_id)
    return render(request, 'employee_app/add_room.html', {"all_hotels":all_hotels})