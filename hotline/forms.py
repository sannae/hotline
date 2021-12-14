from django.forms import ModelForm
from .models import *
from django.apps import apps

def createForm(ModelName):
    app_models = apps.all_models['hotline']
    selectedModel = app_models.get(ModelName)

    class createForm(ModelForm):
        class Meta:
            model = selectedModel
            fields = '__all__'

    return createForm

class ticketForm(ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'
    
class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'

class technicianForm(ModelForm):
    class Meta:
        model = technician
        fields = '__all__'

class productForm(ModelForm):
    class Meta:
        model = product
        fields = '__all__'
