from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
import calendar
import random
from datetime import datetime
from django.apps import apps

# Querysets
all_tickets = ticket.objects.all()
all_customers = customer.objects.all()
all_technicians = technician.objects.all()
all_products = product.objects.all()
all_statuses = status.objects.all()

# Home page
def dashboard(request):
    tickets = all_tickets # .order_by('-updated_at')
    this_month = datetime.today().month
    this_year = datetime.today().year
    days_this_month = calendar.monthrange(9999,this_month)[1]
    list_days = list(range(1,days_this_month+1))

    # Group tickets by status
    tickets_by_status = []
    total_tickets_by_status = []
    status_list = []
    status_colors = []

    for status in all_statuses:

        # Data for pie chart
        status_list.append(status.name)
        status_colors.append(status.color)
        filtered_tickets_by_status = all_tickets.filter(status_id=status.id, updated_at__month=this_month)
        total_tickets_by_status.append(filtered_tickets_by_status.count())

        # Data for stacked bar chart
        status_tickets = []
        for day in list_days:
            # Tickets in the current day
            day_tickets = all_tickets.filter(status_id=status.id, updated_at__year=this_year, updated_at__month=this_month, updated_at__day=day)
            status_tickets.append(day_tickets.count())
        # Add the status name and the tickets list to the tickets_by_status list  
        tickets_by_status.append(status_tickets)

    # No tickets
    if sum(total_tickets_by_status) == 0:
        no_tickets = True
    else:
        no_tickets = False

    context = {
        # General
        'tickets': tickets,
        'customers': all_customers,
        'technicians': all_technicians,
        'current_date': datetime.now(),
        'current_year': this_year,
        'current_month': this_month,
        'current_day': datetime.today().day,
        
        # Pie chart
        'status_colors': status_colors,
        'status_list': status_list,
        'no_tickets': no_tickets,
        'total_tickets_by_status': total_tickets_by_status,

        # Bar chart
        'list_days': list_days,
        'tickets_by_status': tickets_by_status,
    }

    return render(request, 'hotline/dashboard.html', context)

# --- Tickets ---

# Create a new ticket
def new_ticket(request):
    form = createForm("ticket")
    # If the form is submitted
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'ticket_form': form,
        'current_view': request.resolver_match.url_name
    }
    return render(request, 'hotline/ticket_form.html', context)  

# Ticket detail page
def ticket_detail(request, ticket_id):
    my_ticket = get_object_or_404(ticket, pk=ticket_id)
    context = { 'my_ticket': my_ticket, }
    return render(request, 'hotline/ticket_detail.html', context)

# --- Customers ---

# Customer detail page
def customer_detail(request, id):
    my_customer = get_object_or_404(customer, pk=id)
    tickets = all_tickets.filter(customer_id=id).order_by('-updated_at')
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
    form = createForm("customer")
    # If the form is submitted
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'customer_form': form,
        'current_view': request.resolver_match.url_name
    }
    return render(request, 'hotline/customer_form.html', context)  

# --- Technicians ---

# Technician detail page
def technician_detail(request, id):
    my_technician = get_object_or_404(technician, pk=id)
    tickets = all_tickets.filter(technician_id=id).order_by('-updated_at')
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
    form = createForm("technician")
    # If the form is submitted
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'technician_form': form,
        'current_view': request.resolver_match.url_name
    }
    return render(request, 'hotline/technician_form.html', context)  

# --- Products ---

# Product detail page
def product_detail(request, id):
    my_product = get_object_or_404(product, pk=id)
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
    form = createForm("product")
    # If the form is submitted
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'product_form': form,
        'current_view': request.resolver_match.url_name
    }
    return render(request, 'hotline/product_form.html', context)

