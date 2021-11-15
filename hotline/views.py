from django.shortcuts import render
from django.http import HttpResponse
from hotline.models import *

# Querysets
all_tickets = ticket.objects.all()
all_customers = customer.objects.all()

def dashboard(request):
    tickets = all_tickets.order_by('-updated_at')
    customers = all_customers
    technicians = technician.objects.all()

    context = {
        'tickets': tickets,
        'customers': customers,
        'technicians': technicians
    }

    return render(request, 'hotline/dashboard.html', context)

def new_ticket(request):
    return render(request, 'hotline/new_ticket.html')

def customer_detail(request, pk):
    my_customer = customer.objects.get(id=pk)
    tickets = all_tickets.filter(customer_id=pk).order_by('-updated_at')
    context = {
        'my_customer': my_customer,
        'tickets': tickets
    }
    return render(request, 'hotline/customer_detail.html', context)

def customer_list(request):
    customers = all_customers
    context = {
        'customers': customers
    }
    return render(request, 'hotline/customer_list.html', context)

def technician_detail(request, pk):
    my_technician = technician.objects.get(id=pk)
    tickets = all_tickets.filter(technician_id=pk).order_by('-updated_at')
    context = {
        'my_technician': my_technician,
        'tickets': tickets
    }
    return render(request, 'hotline/technician_detail.html', context)