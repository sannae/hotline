# Generated by Django 3.2.9 on 2021-12-30 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0019_auto_20211230_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='priority_id',
        ),
        migrations.AddField(
            model_name='ticket',
            name='priority',
            field=models.IntegerField(choices=[('1', 'low'), ('2', 'medium'), ('3', 'high'), ('4', 'urgent')], default='low'),
        ),
        migrations.DeleteModel(
            name='priority',
        ),
    ]