# Generated by Django 3.2.9 on 2021-12-30 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0022_alter_ticket_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='color',
            field=models.CharField(choices=[('red', 'red'), ('orange', 'orange'), ('grey', 'grey'), ('green', 'green')], default='red', max_length=50),
        ),
    ]
