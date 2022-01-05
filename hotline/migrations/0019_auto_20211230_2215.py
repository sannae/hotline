# Generated by Django 3.2.9 on 2021-12-30 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0018_alter_priority_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priority',
            name='color',
        ),
        migrations.AddField(
            model_name='priority',
            name='level',
            field=models.CharField(choices=[('1', 'low'), ('2', 'medium'), ('3', 'high'), ('4', 'urgent')], default='green', max_length=50),
        ),
    ]