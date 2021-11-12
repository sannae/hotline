from django.shortcuts import render
from django.http import HttpResponse
from hotline.models import *

def dashboard(request):
    tickets = ticket.objects.all().order_by('-updated_at')
    customers = customer.objects.all()
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
    context = {
        'my_customer': my_customer
    }
    return render(request, 'hotline/customer.html', context)

def technician_detail(request, pk):
    my_technician = technician.objects.get(id=pk)
    context = {
        'my_technician': my_technician
    }
    return render(request, 'hotline/technician.html', context)