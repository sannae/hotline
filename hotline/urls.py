from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.dashboard, name='home'),

    # New ticket
    path('new/', views.new_ticket, name='new_ticket'),

    # Customer detail
    path('customer/<str:pk>', views.customer_detail, name="customer_detail"),

    # Customer list
    path('customer_list', views.customer_list, name="customer_list"),

    # Technician detail
    path('technician/<str:pk>', views.technician_detail, name="technician_detail"),

    # Technician list
    path('technician_list', views.technician_list, name="technician_list"),

]