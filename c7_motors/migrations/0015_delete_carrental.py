# Generated by Django 4.0.10 on 2024-09-16 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('c7_motors', '0014_remove_carrental_car_model_remove_carrental_is_paid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarRental',
        ),
    ]
