# Generated by Django 4.0.10 on 2024-07-20 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('c7_motors', '0007_news_delete_report_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('img', models.ImageField(blank=True, default='', upload_to='')),
                ('seats', models.IntegerField()),
                ('gear', models.CharField(choices=[('Manual', 'Manual Transmission'), ('Automatic', 'Automatic Transmission')], max_length=20)),
                ('year', models.CharField(default='', max_length=20)),
                ('miles', models.CharField(blank=True, max_length=100)),
                ('price', models.CharField(blank=True, max_length=100)),
                ('insurnce', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='categories_reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems4', to='c7_motors.cart')),
                ('cate_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items4', to='c7_motors.all_car')),
            ],
        ),
        migrations.CreateModel(
            name='customers_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars', models.TextField(blank=True, default='')),
                ('name', models.TextField(blank=True, default='', max_length=300)),
                ('email', models.TextField(blank=True, default='', max_length=300)),
                ('nationality', models.TextField(blank=True, default='', max_length=300)),
                ('mobile_phone', models.TextField(blank=True, default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='economy_reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='c7_motors.economy_car')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='c7_motors.cart')),
            ],
        ),
        migrations.CreateModel(
            name='luxury_reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems2', to='c7_motors.cart')),
                ('lux_car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items2', to='c7_motors.luxury_car')),
            ],
        ),
        migrations.CreateModel(
            name='premium_reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems3', to='c7_motors.cart')),
                ('pre_car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items3', to='c7_motors.premium_car')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='special_deals_car',
        ),
    ]
