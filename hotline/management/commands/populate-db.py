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
    # Create <amount> customers
    pass

class Command(BaseCommand):
    help = 'Populates the database with random generated data.'

    # Arguments 
    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='The number of orders that should be created.')
        parser.add_argument('--days', type=int, help='The max amount of days in the past')

    # Create customers

    # Create products

    # Create technicians


    def handle(self, *args, **options):
        customers = ticket.objects.all()
        technicians = technician.objects.all()
        products = product.object.all


        amount = options['amount'] if options['amount'] else 2500
        days = options['days'] if options['days'] else 30
        
        for i in range(0, amount):

            # Order made that day
            order = Order.objects.create(
                customer=random.choice(customers),
                product=random.choice(products),
                status=random.choice(statuses)[0],
            )
            # Random day in the last N days
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, days)))
            order.date_created = dt

            # Save date in notes
            order.notes = str(order.date_created)

            # Save in database
            order.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with ' + str(amount) + ' orders!'))