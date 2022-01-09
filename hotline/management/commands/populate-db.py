# management/commands/populate-db.py

# Usage:
# > (env)$ python manage.py populate_db --amount 1000
# To create 1000 random orders

import lorem
import random
from datetime import datetime, timedelta
import pytz
from django.core.management.base import BaseCommand
from hotline.models import *
from hotline.views import new_product

def create_customers(amount):

    customer_names = [
        'ICT Edge',
        'Edu Toys',
        'Mindful Components Ltd',
        'Spotter Spare',
        'Aroma Duck',
        'Dogsquipo',
        'Chefworks',
        'Vehiclehut Inc.',
        'Banana Group',
        'Coco-doodle-doo Brothers'
    ]

    reference_names = [
        'Mitchel Maddox',
        'Yasmin Rangel',
        'Daisy Owen',
        'Roshni Anthony',
        'Summer Woodward',
        'Eilidh Mcleod',
        'Kristofer Morley',
        'Isla-Rose Dudley',
        'Muskaan Petty'
    ]

    customer_addresses = [
        '8509 Ohio Road Columbus, GA 31904',
        '9069 E. Walnutwood Drive Saint Cloud, MN 56301',
        '7661 Ramblewood Street Yuba City, CA 95993',
        '446 Lakeview Street Billings, MT 59101',
        '5 Wagon Dr. Zionsville, IN 46077',
        '177 Pheasant Ave. Ronkonkoma, NY 11779'
    ]

    # Create <amount> customers
    for i in range(0,amount):
        new_customer = customer.objects.create(
            name=random.choice(customer_names),
            reference=random.choice(reference_names),
            reference_phone=str(random.randint(111111,999999)),
            reference_email=random.choice(reference_names)+'@mail.com',
            address=random.choice(customer_addresses),
            phone='+39 '+str(random.randint(1111111,9999999)),
            sw_contract = bool(random.getrandbits(1)),
            hw_contract = bool(random.getrandbits(1))
        )
        # Save in database
        new_customer.save()

def create_department(amount):

    department_names = [
        'Support',
        'IT',
        'Production',
        'Logistics',
        'Customer Service',
        'Development',
        'Quality Assurance',
        'Sales'
    ]

    # Create <amount> departments
    for i in range(0,amount):
        new_department = department.objects.create(
            name=random.choice(department_names)
        )
        # Save in database
        new_department.save()

def create_technician(amount):
    first_names = [
        'John',
        'Jane',
        'Mary',
        'Bob',
        'Sam',
        'Sally',
        'Tom',
        'Alice',
        'Peter',
        'Paul'
    ]
    last_names = [
        'Smith',
        'Jones',
        'Williams',
        'Brown',
        'Davis',
        'Miller',
        'Wilson',
        'Moore',
        'Taylor',
        'Anderson'
    ]
    for i in range(0,amount):
        new_technician = technician.objects.create(
            first_name=random.choice(first_names),
            last_name= random.choice(last_names),
            office_phone = '+39 '+str(random.randint(1111111,9999999)),
            mobile_phone = '+39 '+str(random.randint(1111111,9999999)),
            email = random.choice(first_names)+'.'+random.choice(last_names)+'@mail.com',
            department_id = random.choice(department.objects.all())
        )
        # Save in database
        new_technician.save()

def create_products(amount):
    product_names = [
        'Laptop',
        'Desktop',
        'Tablet',
        'Smartphone',
        'Printer',
        'Scanner',
        'Camera',
        'Projector',
        'Monitor',
        'Speaker',
        'Microphone'
    ]

    for i in range(0,amount):
        new_product = product.objects.create(
            name = random.choice(product_names),
            department_id = random.choice(department.objects.all()),
            description = lorem.sentence()
        )
        # Save in database
        new_product.save()

def create_statuses(amount):
    status_names = [
        'Pending',
        'In Progress',
        'Completed',
        'Cancelled'
    ]
    colors = [
        '#FF0000',
        '#00FF00',
        '#0000FF',
        '#FFFF00',
    ]

    for i in range(0,amount):
        new_status = status.objects.create(
            name = random.choice(status_names),
            color = random.choice(colors)
        )
        # Save in database
        new_status.save()



class Command(BaseCommand):
    help = 'Populates the database with random generated data.'

    # Arguments 
    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='The number of orders that should be created.')
        parser.add_argument('--days', type=int, help='The max amount of days in the past')

    def handle(self, *args, **options):

        amount = options['amount'] if options['amount'] else 5
        days = options['days'] if options['days'] else 2
        
        # In order of dependencies:
        create_customers(amount)
        create_department(amount)
        create_technician(amount)
        create_products(amount)
        create_statuses(amount)
        # create_tickets

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with ' + 
        str(amount) + ' objects!'))