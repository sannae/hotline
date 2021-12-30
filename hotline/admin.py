from django.contrib import admin
from .models import *

admin.site.register(ticket)
admin.site.register(technician)
admin.site.register(product)
admin.site.register(department)
admin.site.register(customer)
admin.site.register(status)

