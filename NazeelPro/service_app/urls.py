
from django.urls import path
from . import views

app_name = 'service_app'
urlpatterns = [
    path('',views.service,name='service'),
    path('manager/',views.manager_services,name='manager_services'),
    path("menu/<main_services_id>/",views.menu,name='menu'),
    path("add/",views.add_service,name='add_service'),
    path("edit/items/<main_services_id>/",views.edit_items,name='edit_items'),
    path("order/request/", views.submit_request, name='order_request'),
    path("order/request/update/<request_id>/", views.update_request, name='update_request'),
    path("active/order/<main_services_id>/",views.active_order,name='active_order'),
    path("delete/item/<item_id>/",views.delete_items,name='delete_items'),
    path("edit/<main_services_id>/",views.edit_main_service,name='edit_main_service'),
    path("delete/service/<main_services_id>/",views.delete_service,name='delete_service'),

]
