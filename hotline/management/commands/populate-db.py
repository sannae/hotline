# management/commands/populate_db.py

# Usage:
# > (env)$ python manage.py populate_db --amount 1000
# To create 1000 random orders

import random
from datetime import datetime, timedelta
import pytz
from django.core.management.base import BaseCommand
from hotline.models import *

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

    # Create <amount> customers
    for i in range(0,amount):
        customer = customer.objects.create(
            name=random.choice(customer_names),
            reference=random.choice(reference_names),
            reference_phone=str(random.randint(111111,999999))
            reference_email=random.choice(reference_names)+'@mail.com'
            address=random.choice(customer_addresses)
            phone='+39 '+str(random.randint(1111111,9999999))
            sw_contract = bool(random.getrandbits(1))
            hw_contract = bool(random.getrandbits(1))
        )
        # Save in database
        customer.save()

class Command(BaseCommand):
    help = 'Populates the database with random generated data.'

    # Arguments 
    # def add_arguments(self, parser):
    #    parser.add_argument('--amount', type=int, help='The number of orders that should be created.')
    #    parser.add_argument('--days', type=int, help='The max amount of days in the past')

    # Create customers

    # Create products

    # Create technicians

    def handle(self, *args, **options):
        # customers = ticket.objects.all()
        # technicians = technician.objects.all()
        # products = product.object.all

        amount = options['amount'] if options['amount'] else 5
        days = options['days'] if options['days'] else 2
        
        create_customers(amount)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with ' + str(amount) + ' customers!'))