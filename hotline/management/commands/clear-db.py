# management/commands/clear-db.py

# Usage:
# > (env)$ python -m manage clear-db

from django.core.management.base import BaseCommand
from hotline.models import *
from django.apps import apps

# Selecting only models from app
app_models = apps.all_models['hotline']
for model in app_models:
    selectedModel.objects.all().delete(app_models.get(model))

class Command(BaseCommand):
    help = 'Clear the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully cleared the database.'))