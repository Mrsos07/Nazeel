
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpRequest
from service_app.models import MainService , SubService, Review , SubServiceRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
# Create your views here.
from guest_app.models import Guest

from main_app.models import Hotel


def home(request: HttpRequest):
    """Rendering the home page template"""
    services = MainService.objects.all()[:3]
    return render(request, 'main_app/home.html', {"services": services})

@login_required
def history(request: HttpRequest):
    """Rendering the history page template"""
    try:
        main_services = MainService.objects.all()
        guest = Guest.objects.get(name=request.user.username)
        user_requests = SubServiceRequest.objects.filter(room=guest.room)

        return render(request, 'main_app/history.html', {"user_requests": user_requests})
    except:
        return render(request,'main_app/home.html')

@login_required
def order(request: HttpRequest, main_services_id):
    try:
        sub_services_all = SubService.objects.all()
        main_services = MainService.objects.get(id=main_services_id)
        sub_service = SubService.objects.filter(main_service=main_services)
        guest = Guest.objects.get(name=request.user.username)


        total_price = 0
        context = {
            'sub_service': sub_service,
            'total_price': total_price,
            'sub_service_all': sub_services_all,
            'main_service': main_services,
            "guest": guest
        }


        return render(request, 'main_app/order.html', context)
    except:
        return redirect('main_app:home')


def maps(request:HttpRequest):
    return render(request,'main_app/maps.html')





@csrf_exempt
@login_required
def chatbot(request):
        try:
            if request.method == 'POST':
                data = json.loads(request.body)
                clean_data = list(data.values())

                # Remove leading and trailing whitespace from each value
                clean_data = [value.strip() for value in clean_data]

                # Access the clean text or join the values together
                clean_text = ' '.join(clean_data)
                user_input = request.POST.get('message')
                print(clean_text)
                # Define the chatbot's responses for different questions
                answer_list=['please choose one :\n\n'
                             '-check in \n\n\n'
                             '-check out \n\n\n'
                             '-breakfast\n\n\n'
                             '-wifi\n\n'
                             '-room service\n\n'
                             '-pool\n\n'
                             '-restaurant\n\n']

                responses = {
                    'hi': 'Hello! How can I assist you today?',
                    'hello': 'Hello! How can I assist you today?',
                    'check in': 'The check-in time is at 3:00 PM.',
                    'check out': 'The check-out time is at 11:00 AM.',
                    'breakfast': 'Yes, we offer complimentary breakfast for all guests.',
                    'parking': 'Yes, we have free parking available for our guests.',
                    'wifi': 'Yes, we provide free Wi-Fi access in all rooms and public areas.',
                    'room service': 'Yes, we offer 24-hour room service.',
                    'pool': 'Yes, we have an outdoor pool for guests to enjoy.',
                    'gym': 'Yes, we have a fully equipped gym available for guests to use.',
                    'thank you': 'You\'re welcome! If you have any more questions, feel free to ask.',
                    'by': 'Goodbye! Have a great day!'

                    }

                responses_more={
                    'restaurant': 'Yes, we have an on-site restaurant that serves breakfast, lunch, and dinner.',
                    'room types': 'We offer a variety of room types including standard rooms, suites, and deluxe rooms.',
                    'amenities': 'Our hotel amenities include a spa, concierge service, business center, and laundry facilities.',
                    'pet-friendly': 'Yes, we are a pet-friendly hotel. Additional charges may apply.',
                    'cancellation policy': 'Our cancellation policy allows free cancellation up to 24 hours before check-in.',
                    'local attractions': 'Some popular local attractions near our hotel include museums, parks, and shopping centers.',
                    'nearest airport': 'The nearest airport is XYZ Airport, located approximately 10 miles away from our hotel.',
                    'special offers': 'We have special offers and packages available. Please visit our website for more details.',
                }

                # Check if the user's message matches any of the predefined questions
                if clean_text in responses :
                    return JsonResponse({'response': responses[clean_text]})
                elif clean_text in responses_more:
                    return JsonResponse({'response': responses_more[clean_text]})

                # If the user's message doesn't match any predefined questions, provide a default response
                return JsonResponse({'response': answer_list})

            return render(request, 'main_app/chatbot.html')
        except:
            return redirect('main_app:home')


def services(request: HttpRequest):
    try:
        return render(request, 'main_app/services.html')
    except:
        return redirect('main_app:home')

def about(request: HttpRequest):
    return render(request, 'main_app/about.html')



def logout_page(request: HttpRequest):
    logout(request)
    return redirect('main_app:home')

def add_review(request: HttpRequest):
    try:
        if request.method == "POST":

            new_review = Review(
                 name= request.POST['name'],content=request.POST["content"], rating=request.POST["rating"])
            new_review.save()


            return redirect("service_app:service")
    except:
        return redirect('main_app:home')


def entertainment(request: HttpRequest):
    try:
        hotel = Hotel.objects.first()  # Get a specific hotel instance
        city = hotel.city.lower()  # Access the city attribute of the hotel

        saudi_vist = f"https://www.visitsaudi.com/en/see-do/destinations/{city}"
        return redirect(saudi_vist)
    except:
        return redirect('main_app:home')

