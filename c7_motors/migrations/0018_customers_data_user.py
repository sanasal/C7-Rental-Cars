# Generated by Django 4.0.10 on 2024-09-22 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('c7_motors', '0017_alter_all_car_price_alter_customers_data_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers_data',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
