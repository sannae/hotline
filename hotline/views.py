from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import datetime

# Querysets
all_tickets = ticket.objects.all()
all_customers = customer.objects.all()
all_technicians = technician.objects.all()
all_products = product.objects.all()

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

# Ticket detail page
def ticket_detail(request, pk):
    my_ticket = ticket.objects.get(id=pk)
    context = {
        'my_ticket': my_ticket,
    }
    return render(request, 'hotline/ticket_detail.html', context)

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
    context = {
        'customers': all_customers,
    }
    return render(request, 'hotline/customer_list.html', context)

# Create a new ticket
def new_customer(request):
    form = customerForm()

    # If the form is submitted
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'new_customer_form': form
    }
    return render(request, 'hotline/new_customer.html', context)

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
    context = {
        'technicians': all_technicians
    }
    return render(request, 'hotline/technician_list.html', context)

# Create a new technician
def new_technician(request):
    form = technicianForm()

    # If the form is submitted
    if request.method == 'POST':
        form = technicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'new_technician_form': form
    }
    return render(request, 'hotline/new_technician.html', context)

# --- Products ---

# Product detail page
def product_detail(request, pk):
    my_product = product.objects.get(id=pk)
    context = {
        'my_product': my_product,
    }
    return render(request, 'hotline/product_detail.html', context)

# List of products
def product_list(request):
    context = {
        'products': all_products
    }
    return render(request, 'hotline/product_list.html', context)

# Create a new product
def new_product(request):
    form = productForm()

    # If the form is submitted
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'new_product_form': form
    }
    return render(request, 'hotline/new_product.html', context)