# Generated by Django 4.0.10 on 2024-09-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c7_motors', '0022_remove_customers_data_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers_data',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
