
from django.urls import path
from . import views

app_name = 'service_app'
urlpatterns = [
    path('',views.service,name='service'),
    path("menu/",views.menu,name='menu'),
    path("add/",views.add_service,name='add_service'),
    path("edit/items/",views.edit_items,name='edit_items'),
    path("order/request/",views.order_request,name='order_request'),
    path("active/order/",views.active_order,name='active_order'),
]