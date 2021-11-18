from django.forms import ModelForm
from .models import *

class ticketForm(ModelForm):
    class Meta:
        model = ticket
        labels = {
            "customer_id": "Cliente",
            "technician_id": "Tecnico",
            "products": "Prodotti",
            "title": "Titolo",
            "notes": "Descrizione",
            "duration": "Durata",
            "status_id": "Stato",
            "priority_id": "Priorità",
            "order_number": "Numero Ordine"
        }
        fields = [
            'customer_id',
            'technician_id',
            'products',
            'title',
            'notes',
            'duration',
            'status_id',
            'priority_id',
            'order_number'
        ]
    
class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'

class technicianForm(ModelForm):
    class Meta:
        model = technician
        fields = '__all__'