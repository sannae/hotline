from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey

# A ticket is an element of support activity
class ticket(models.Model):

    PRIORITY_LEVELS = [
        ('1','low'),
        ('2','medium'),
        ('3','high'),
        ('4','urgent')
    ]

    # id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey('customer', on_delete=models.PROTECT)
    technician_id = models.ForeignKey('technician', on_delete=models.PROTECT)
    products = models.ManyToManyField('product', blank=True)
    title = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    duration = models.IntegerField()
    status_id = models.ForeignKey('status', default='1', on_delete=models.PROTECT)
    priority = models.CharField(max_length=10, default='low', choices=PRIORITY_LEVELS, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_number = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.title.upper() + ' for ' + self.customer_id.name.upper() + ' by ' + self.technician_id.last_name.upper()

class technician(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=15, null=True, blank=True)
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True) 
    department_id = ForeignKey('department', on_delete=models.PROTECT)
    def __str__(self):
        return self.last_name

class product(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department_id = ForeignKey('department', on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
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
    reference_phone = models.CharField(max_length=50, null=True, blank=True)
    reference_email = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    sw_contract = BooleanField(default=False)
    hw_contract = BooleanField(default=False)
    def __str__(self):
        return self.name

class status(models.Model):

    STATUS_COLORS = [     # Values from pill badges in Bootstrap
        ('red','red'),    
        ('orange','orange'), 
        ('grey','grey'), 
        ('green','green')
    ]

    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, default='pending')
    color = models.CharField(max_length=50, default='red', choices=STATUS_COLORS)
    def __str__(self):
        return self.name
