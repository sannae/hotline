# Generated by Django 3.2.9 on 2021-11-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0010_alter_ticket_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]