# Generated by Django 3.2.6 on 2021-11-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
