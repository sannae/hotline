from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.dashboard, name='home'),

    # ---- Tickets ----

    path('new_ticket/', views.new_ticket, name='new_ticket'),
    path('ticket/<str:ticket_id>', views.ticket_detail, name="ticket_detail"),

    # --- Customers ---

    path('new_customer/', views.new_customer, name='new_customer'),
    path('customer/<str:id>', views.customer_detail, name="customer_detail"),
    path('customer_list', views.customer_list, name="customer_list"),

    # --- Technicians ---

    path('new_technician/', views.new_technician, name='new_technician'),
    path('technician/<str:id>', views.technician_detail, name="technician_detail"),
    path('technician_list', views.technician_list, name="technician_list"),

    # --- Products ---

    path('new_product/', views.new_product, name='new_product'),
    path('product/<str:id>', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),

]