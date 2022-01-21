# management/commands/populate-db.py

# Usage:
# > (env)$ python manage.py populate_db --amount 10 --days 30
# To create 10 random objects with datetime properties included in the last 30 days
# NOTE: The previous records are cleared out, use for test purposes only!

import lorem
import random, string
from datetime import datetime, timedelta
import pytz
from django.core.management.base import BaseCommand
from django.core import management
from hotline.models import *
from hotline.views import new_product, product_list

def random_date(days):
    start_date = datetime.now(pytz.timezone('Europe/Rome'))
    end_date = start_date - timedelta(days=random.randint(0,days)) - timedelta(hours=random.randint(0,24)) - timedelta(minutes=random.randint(0,60))

    return end_date

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
            email = '',
            department_id = random.choice(department.objects.all())
        )
        # Set email
        new_technician.email = new_technician.first_name + '.' + new_technician.last_name + '@mail.com'
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
            name = random.choice(product_names) + 
            ' ' + ''.join(random.choice(string.ascii_uppercase) for i in range(5)),
            department_id = random.choice(department.objects.all()),
            description = lorem.sentence()
        )
        # Save in database
        new_product.save()

def create_statuses(amount):

    statuses = [
        ("Pending","red"),
        ("In Progress","orange"),
        ("Completed","green"),
        ("Cancelled","grey")
    ]

    for i in list(range(0,len(statuses))):
        new_status = status.objects.create(
            name = statuses[i][0],
            color = statuses[i][1]
        )
        # Save in database
        new_status.save()

def create_tickets(amount,days):

    for i in range(0,amount):

        PRIORITY_LEVELS = [
            ('1','Low'),
            ('2','Medium'),
            ('3','High'),
            ('4','Urgent')
        ]

        new_ticket = ticket.objects.create(
            customer_id = random.choice(customer.objects.all()),
            technician_id = random.choice(technician.objects.all()),
            title = lorem.sentence(),
            duration = random.randint(1,480),
            created_at = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, days))), # random_date(days),
            updated_at = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, days))), #random_date(days),
            priority = random.choice([level[0] for level in PRIORITY_LEVELS]),
            status_id = random.choice(status.objects.all()),
            notes = lorem.paragraph(),         
        )

        # Multiple products
        total_statuses = status.objects.all().count()
        for i in range(random.randint(1,total_statuses)):
            new_ticket.products.add(random.choice(product.objects.all()))

        new_ticket.save()


class Command(BaseCommand):
    help = 'Populates the database with random generated data.'

    # Arguments 
    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='The number of orders that should be created.')
        parser.add_argument('--days', type=int, help='The max amount of days in the past')

    def handle(self, *args, **options):

        amount = options['amount'] if options['amount'] else 5
        days = options['days'] if options['days'] else 30

        # Clear the db first
        # management.call_command("clear-db") 

        # Create objects only if not pre-existent
        if not customer.objects.all():
            create_customers(amount)
        if not department.objects.all():
            create_department(amount)
        if not technician.objects.all():
            create_technician(amount)
        if not product.objects.all():
            create_products(amount)
        if not status.objects.all():
            create_statuses(amount)

        # Create tickets nevertheless
        create_tickets(amount,days)

        # Success message
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with ' + 
        str(amount) + ' objects!'))
