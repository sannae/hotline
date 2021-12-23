# Generated by Django 3.2.9 on 2021-12-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0013_alter_priority_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='color',
            field=models.CharField(choices=[('bg-danger', 'bg-danger'), ('orange', 'bg-warning'), ('white', 'bg-light'), ('green', 'bg-success')], default='green', max_length=50),
        ),
    ]
