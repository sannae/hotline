from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey

# A ticket is an element of support activity
class ticket(models.Model):
    # id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey('customer', on_delete=models.PROTECT) # Related customer
    technician_id = models.ForeignKey('technician', on_delete=models.PROTECT) # Assigned technician
    products = models.ManyToManyField('product', blank=True) # Product, one or many
    title = models.CharField(max_length=255) # main title of the ticket
    updated_at = models.DateTimeField(auto_now=True) # Last update
    notes = models.TextField() # Ticket main description
    duration = models.IntegerField() # duration in minutes
    status_id = models.ForeignKey('status', on_delete=models.PROTECT)
    priority_id = models.ForeignKey('priority', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    order_number = models.IntegerField()
    def __str__(self):
        return self.id

class technician(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department_id = ForeignKey('department', on_delete=models.PROTECT)
    def __str__(self):
        return self.last_name

class product(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department_id = ForeignKey('department', on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class department(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    subset = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class customer(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    sw_contract = BooleanField(default=False)
    hw_contract = BooleanField(default=False)
    def __str__(self):
        return self.name

class status(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, default='pending')
    color = models.CharField(max_length=50, default='red')

class priority(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, default='low')
    color = models.CharField(max_length=50, default='green')
