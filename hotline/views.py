from django.shortcuts import redirect, render
from django.http import HttpResponse
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
    tickets = all_tickets.order_by('-updated_at')
    current_year = datetime.now().year

    # Group tickets by status
    total_tickets_by_status = []
    status_list = []
    status_colors = []
    for status in all_statuses:
        status_list.append(status.name)
        status_colors.append(status.color)
        # Random colors
        # status_colors.append('rgb('+str(random.randint(0,255))+','+str(random.randint(0,255))+','+str(random.randint(0,255))+')')
        filtered_tickets_by_status = all_tickets.filter(status_id=status.id)
        total_tickets_by_status.append(filtered_tickets_by_status.count())

    if sum(total_tickets_by_status) == 0:
        no_tickets = True
    else:
        no_tickets = False

    tickets_by_status = []
    this_month = datetime.today().month
    this_year = datetime.today().year
    days_this_month = calendar.monthrange(9999,this_month)[1]
    list_days = list(range(1,days_this_month+1))
    for status in all_statuses:  
        status_tickets = []
        for day in list_days:
            # Tickets in the current day
            day_tickets = all_tickets.filter(status_id=status.id, updated_at__year=this_year, created_at__month=this_month, created_at__day=day)
            status_tickets.append(day_tickets.count())
        # Add the status name and the tickets list to the tickets_by_status list  
        tickets_by_status.append(status_tickets)

    context = {
        # General
        'tickets': tickets,
        'customers': all_customers,
        'technicians': all_technicians,
        'current_year': current_year,
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

# Update ticket
def update_ticket(request, pk):
    ticket = all_tickets.get(id=pk)
    form = ticketForm(instance=ticket)
    if request.method == "POST":
        form = ticketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'ticket_form': form,
        'current_view': request.resolver_match.url_name
    }
    return render(request, 'hotline/ticket_form.html', context)

# Ticket detail page
def ticket_detail(request, pk):
    my_ticket = ticket.objects.get(id=pk)
    context = {
        'my_ticket': my_ticket,
    }
    return render(request, 'hotline/ticket_detail.html', context)

def delete(request, pk):

    # TODO: Do *not* depend on the object, here instantiated explicitely
    obj = "ticket"

    # Object to be deleted
    app_models = apps.all_models['hotline']
    selectedModel = app_models.get(obj)
    object = selectedModel.objects.get(id=pk)

    # Actual deletion
    if request.method == "POST":
        object.delete()
        # Go back to home
        return redirect('/')

    context = {
    }

    return render(request, 'hotline/delete_confirm.html', context)

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

# Update ticket
def update_customer(request, pk):
    customer = all_customers.get(id=pk)
    form = customerForm(instance=customer)
    if request.method == "POST":
        form = customerForm(request.POST, instance=customer)
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

# Update technician
def update_technician(request, pk):
    technician = all_technicians.get(id=pk)
    form = technicianForm(instance=technician)
    if request.method == "POST":
        form = technicianForm(request.POST, instance=technician)
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

# Update product
def update_product(request, pk):
    product = all_products.get(id=pk)
    form = productForm(instance=product)
    if request.method == "POST":
        form = productForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'product_form': form,
        'current_view': request.resolver_match.url_name
    }
    return render(request, 'hotline/product_form.html', context)
