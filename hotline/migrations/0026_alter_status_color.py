# Generated by Django 3.2.9 on 2022-01-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0025_alter_status_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='color',
            field=models.CharField(choices=[('red', 'red'), ('orange', 'orange'), ('green', 'green'), ('grey', 'grey')], default='red', max_length=50),
        ),
    ]