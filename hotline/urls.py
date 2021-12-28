from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.dashboard, name='home'),

    # ---- Tickets ----

    path('new_ticket/', views.new_ticket, name='new_ticket'),
    path('ticket/<str:pk>', views.ticket_detail, name="ticket_detail"),
    path('update_ticket/<str:pk>', views.update_ticket, name="update_ticket"),
    path('delete/<str:pk>', views.delete, name="delete"),

    # --- Customers ---

    path('new_customer/', views.new_customer, name='new_customer'),
    path('customer/<str:pk>', views.customer_detail, name="customer_detail"),
    path('customer_list', views.customer_list, name="customer_list"),
    path('update_customer/<str:pk>', views.update_customer, name="update_customer"),

    # --- Technicians ---

    path('new_technician/', views.new_technician, name='new_technician'),
    path('technician/<str:pk>', views.technician_detail, name="technician_detail"),
    path('technician_list', views.technician_list, name="technician_list"),
    path('update_technician/<str:pk>', views.update_technician, name="update_technician"),

    # --- Products ---

    path('new_product/', views.new_product, name='new_product'),
    path('product/<str:pk>', views.product_detail, name='product_detail'),
    path('product_list/', views.product_list, name='product_list'),
    path('update_product/<str:pk>', views.update_product, name="update_product"),

]