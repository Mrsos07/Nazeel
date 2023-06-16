
from django.urls import path
from . import views

app_name = 'guest_app'
urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('guest_home/', views.guest_home, name='guest_home'),
]
