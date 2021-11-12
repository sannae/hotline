from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.dashboard, name='home'),

    # New ticket
    path('new/', views.new_ticket, name='new_ticket'),

    # Customer detail
    path('customer/<str:pk>', views.customer_detail, name="customer_detail"),

    # Technician detail
    path('technician/<str:pk>', views.technician_detail, name="technician_detail"),
]