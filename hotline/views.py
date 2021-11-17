from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import datetime

# Querysets
all_tickets = ticket.objects.all()
all_customers = customer.objects.all()
all_technicians = technician.objects.all()

# Home page
def dashboard(request):
    tickets = all_tickets.order_by('-updated_at')

    context = {
        'tickets': tickets,
        'customers': all_customers,
        'technicians': all_technicians
    }

    return render(request, 'hotline/dashboard.html', context)

# --- Tickets ---

# Create a new ticket
def new_ticket(request):
    form = ticketForm()

    # If the form is submitted
    if request.method == 'POST':
        form = ticketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'new_ticket_form': form
    }
    return render(request, 'hotline/new_ticket.html', context)

# --- Customers ---

# Customer detail page
def customer_detail(request, pk):
    my_customer = customer.objects.get(id=pk)
    tickets = all_tickets.filter(customer_id=pk).order_by('-updated_at')
    current_year = datetime.now().year
    context = {
        'my_customer': my_customer,
        'tickets': tickets,
        'current_year': current_year
    }
    return render(request, 'hotline/customer_detail.html', context)

# List of customers
def customer_list(request):
    customers = all_customers
    context = {
        'customers': customers
    }
    return render(request, 'hotline/customer_list.html', context)

# Create a new customer
def new_customer(request):
    return render(request, 'hotline/new_customer.html')

# --- Technicians ---

# Technician detail page
def technician_detail(request, pk):
    my_technician = technician.objects.get(id=pk)
    tickets = all_tickets.filter(technician_id=pk).order_by('-updated_at')
    context = {
        'my_technician': my_technician,
        'tickets': tickets
    }
    return render(request, 'hotline/technician_detail.html', context)

# List of technicians
def technician_list(request):
    technicians = all_technicians
    context = {
        'technicians': technicians
    }
    return render(request, 'hotline/technician_list.html', context)
