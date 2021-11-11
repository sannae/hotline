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