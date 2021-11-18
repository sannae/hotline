from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.dashboard, name='home'),

    # ---- Tickets ----

    path('new_ticket/', views.new_ticket, name='new_ticket'),
    path('ticket/<str:pk>', views.ticket_detail, name="ticket_detail"),

    # --- Customers ---

    path('new_customer/', views.new_customer, name='new_customer'),
    path('customer/<str:pk>', views.customer_detail, name="customer_detail"),
    path('customer_list', views.customer_list, name="customer_list"),

    # --- Technicians ---

    path('new_technician/', views.new_technician, name='new_technician'),
    path('technician/<str:pk>', views.technician_detail, name="technician_detail"),
    path('technician_list', views.technician_list, name="technician_list"),

]