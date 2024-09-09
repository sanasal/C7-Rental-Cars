from django.db import models
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here

class customers_data(models.Model):
    cars = models.TextField(default='', blank=True)
    name = models.TextField(max_length=300, default='', blank=True)
    email = models.TextField(max_length=300, default='', blank=True)
    nationality = models.TextField(max_length=300, default='', blank=True)
    mobile_phone = models.TextField(blank=True, default='')
    amount = models.TextField(blank=True,default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cars} - {self.name} - ${self.amount}"

class all_car(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    seats = models.IntegerField()
    
    MANUAL = 'Manual'
    AUTOMATIC = 'Automatic'
    GEAR_CHOICES = [
        (MANUAL, 'Manual Transmission'),
        (AUTOMATIC, 'Automatic Transmission'),
    ]
    
    gear = models.CharField(max_length=20, choices=GEAR_CHOICES)
    year = models.CharField(max_length=20 , default='')
    miles = models.CharField(max_length=100 , blank=True)
    price =models.CharField(max_length=100 , blank=True)
    insurnce = models.CharField(max_length=100 , blank=True)

    def __str__(self):
        return f"{self.name}"

class news(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    seats = models.IntegerField()
    
    MANUAL = 'Manual'
    AUTOMATIC = 'Automatic'
    GEAR_CHOICES = [
        (MANUAL, 'Manual Transmission'),
        (AUTOMATIC, 'Automatic Transmission'),
    ]
    
    gear = models.CharField(max_length=20, choices=GEAR_CHOICES)
    year = models.CharField(max_length=20 , default='')
    miles = models.CharField(max_length=100 , blank=True)
    price =models.CharField(max_length=100 , blank=True)
    insurnce = models.CharField(max_length=100 , blank=True)

    def __str__(self):
        return f"{self.name}"


class economy_car(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    seats = models.IntegerField()
    
    MANUAL = 'Manual'
    AUTOMATIC = 'Automatic'
    GEAR_CHOICES = [
        (MANUAL, 'Manual Transmission'),
        (AUTOMATIC, 'Automatic Transmission'),
    ]
    
    gear = models.CharField(max_length=20, choices=GEAR_CHOICES)
    year = models.CharField(max_length=20 , default='')
    miles = models.CharField(max_length=100 , blank=True)
    price =models.CharField(max_length=100 , blank=True)
    insurnce = models.CharField(max_length=100 , default='')

    def __str__(self):
        return f"{self.name}"


class premium_car(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    seats = models.IntegerField()
    
    MANUAL = 'Manual'
    AUTOMATIC = 'Automatic'
    GEAR_CHOICES = [
        (MANUAL, 'Manual Transmission'),
        (AUTOMATIC, 'Automatic Transmission'),
    ]
    
    gear = models.CharField(max_length=20, choices=GEAR_CHOICES)
    year = models.CharField(max_length=20 , default='')
    miles = models.CharField(max_length=100 , blank=True)
    price =models.CharField(max_length=100 , blank=True)
    insurnce = models.CharField(max_length=100 ,default='')


    def __str__(self):
        return f"{self.name}"


class luxury_car(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(default = '' , blank=True)
    seats = models.IntegerField()
    
    MANUAL = 'Manual'
    AUTOMATIC = 'Automatic'
    GEAR_CHOICES = [
        (MANUAL, 'Manual Transmission'),
        (AUTOMATIC, 'Automatic Transmission'),
    ]
    
    gear = models.CharField(max_length=20, choices=GEAR_CHOICES)
    year = models.CharField(max_length=20 , default='')
    miles = models.CharField(max_length=100 , blank=True)
    price =models.CharField(max_length=100 , blank=True)
    insurnce = models.CharField(max_length=100 , blank=True , default='')


    def __str__(self):
        return f"{self.name}"
   
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4 , primary_key=True)
    user = models.ForeignKey(User,null = True, on_delete = models.SET_NULL) 
    completed =  models.BooleanField(default=False)
     
    def __str__(self):
       return str(self.id)


class economy_reservation(models.Model):
    car = models.ForeignKey(economy_car, on_delete=models.CASCADE , related_name='items')
    price = models.ForeignKey(economy_car, on_delete=models.CASCADE , related_name='price_items')
    insurnce = models.ForeignKey(economy_car, on_delete=models.CASCADE , related_name='insurnce_items')
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE , related_name='cartitems')

    def __str__(self):
       return self.car.name

class luxury_reservation(models.Model):
    lux_car = models.ForeignKey(luxury_car, on_delete = models.CASCADE , related_name='items2' , null=True)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE , related_name='cartitems2')

    def __str__(self):
       return self.lux_car.name

    def __str__(self):
       return self.lux_car.price

    def __str__(self):
       return self.lux_car.insurnce


class premium_reservation(models.Model):
    pre_car = models.ForeignKey(premium_car, on_delete = models.CASCADE , related_name='items3' , null =True)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE , related_name='cartitems3')
   
    def __str__(self):   
        return self.pre_car.name

    def __str__(self):
       return self.pre_car.price
    
    def __str__(self):
       return self.pre_car.insurnce

class categories_reservation(models.Model):
    cate_car = models.ForeignKey(all_car, on_delete=models.CASCADE , related_name='items4')
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE , related_name='cartitems4')

    def __str__(self):
       return self.cate_car.name

    def __str__(self):
       return self.cate_car.price

    def __str__(self):
       return self.cate_car.insurnce
