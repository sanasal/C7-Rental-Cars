#models.py
from django.db import models
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4 , primary_key=True)
    user = models.ForeignKey(User,null = True, on_delete = models.SET_NULL) 
    completed =  models.BooleanField(default=False)
     
    def __str__(self):
       return f"{self.id} - {self.user}"
class customers_data(models.Model):
    user = models.ForeignKey(User,null = True, on_delete = models.SET_NULL) 
    cars = models.TextField(default='', blank=True)
    name = models.TextField(max_length=300, default='', blank=True)
    email = models.TextField(max_length=300, default='', blank=True)
    nationality = models.TextField(max_length=300, default='', blank=True)
    mobile_phone = models.TextField(blank=True, default='')
    price =models.IntegerField(null=True)
    pick_up_date = models.DateField(null=True, blank=True)
    pick_up_time = models.TimeField(null=True, blank=True)
    drop_off_date = models.DateField(null=True, blank=True)
    drop_off_time = models.TimeField(null=True, blank=True)
    
    def total_price(self):
        if not self.pick_up_date or not self.drop_off_date:
            return None 

        total_days = (self.drop_off_date - self.pick_up_date).days + 1
        cart = Cart.objects.get(user=self.user, completed=False)

        cartitems = cart.cartitems.all()
        cartitems2 = cart.cartitems2.all()
        cartitems3= cart.cartitems3.all()
        cartitems4= cart.cartitems4.all()

        economy_total = sum([item.economy_cars_price() for item in cartitems])
        luxury_total = sum([item.luxury_cars_price() for item in cartitems2])
        premium_total = sum ([item.premium_cars_price() for item in cartitems3])
        categories_total = sum ([item.categories_cars_price() for item in cartitems4])
        total_price_without_discount = economy_total + luxury_total + premium_total + categories_total

        total_dicount = 0
        if total_days >= 7:
            total_dicount=10
        if total_days >= 30:
            total_dicount=30
        if total_days >= 90 :
            total_dicount=50
        if total_days >= 365:
            total_dicount=65
        discount = total_dicount / 100
        total_price_after_discount = total_price_without_discount - (total_price_without_discount * discount)

        self.price = total_price_after_discount
        self.save(update_fields=['price'])

        return int(total_price_after_discount)

    def __str__(self):
        return f"cars:{self.cars} - user:{self.user} - name:{self.name}"

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
    price =models.IntegerField()
    insurance = models.IntegerField()

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
    price =models.IntegerField()
    insurance = models.IntegerField()

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
    price =models.IntegerField()
    insurance = models.IntegerField()


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
    price =models.IntegerField()
    insurance = models.IntegerField()


    def __str__(self):
        return f"{self.name}"
   


class economy_reservation(models.Model):
    car = models.ForeignKey(economy_car, on_delete=models.CASCADE , related_name='items')
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE , related_name='cartitems')

    def __str__(self):
        return f"{self.car.name} - {self.car.insurance} - ${self.car.price}"

    def economy_cars_price(self):
        # Get the latest customers_data for the user associated with the cart
        latest_customer_data = self.cart.user.customers_data_set.latest('id')

        # Calculate total days based on pick_up_date and drop_off_date
        total_days = (latest_customer_data.drop_off_date - latest_customer_data.pick_up_date).days + 1

        eco_car_price_per_day=int(self.car.price)
        eco_car_insurance = int(self.car.insurance)
        eco_car_price_for_days = eco_car_price_per_day*total_days
        eco_cars_total_price = eco_car_insurance + eco_car_price_for_days
        return eco_cars_total_price


    

class luxury_reservation(models.Model):
    lux_car = models.ForeignKey(luxury_car, on_delete = models.CASCADE , related_name='items2' , null=True)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE , related_name='cartitems2')

    def __str__(self):
        return f"{self.lux_car.name} - {self.lux_car.insurance} - ${self.lux_car.price}"

    def luxury_cars_price(self):
        # Get the latest customers_data for the user associated with the cart
        latest_customer_data = self.cart.user.customers_data_set.latest('id')

        # Calculate total days based on pick_up_date and drop_off_date
        total_days = (latest_customer_data.drop_off_date - latest_customer_data.pick_up_date).days + 1

        lux_car_price_per_day=int(self.lux_car.price)
        lux_car_insurance = int(self.lux_car.insurance)
        lux_car_price_for_days = lux_car_price_per_day*total_days
        lux_cars_total_price = lux_car_insurance + lux_car_price_for_days
        return lux_cars_total_price


class premium_reservation(models.Model):
    pre_car = models.ForeignKey(premium_car, on_delete = models.CASCADE , related_name='items3' , null =True)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE , related_name='cartitems3')
   
    def __str__(self):
        return f"{self.pre_car.name} - {self.pre_car.insurance} - ${self.pre_car.price}"

    def premium_cars_price(self):
        # Get the latest customers_data for the user associated with the cart
        latest_customer_data = self.cart.user.customers_data_set.latest('id')

        # Calculate total days based on pick_up_date and drop_off_date
        total_days = (latest_customer_data.drop_off_date - latest_customer_data.pick_up_date).days + 1

        pre_car_price_per_day=int(self.pre_car.price)
        pre_car_insurance = int(self.pre_car.insurance)
        pre_car_price_for_days = pre_car_price_per_day*total_days
        pre_cars_total_price = pre_car_insurance + pre_car_price_for_days
        return pre_cars_total_price

class categories_reservation(models.Model):
    cate_car = models.ForeignKey(all_car, on_delete=models.CASCADE , related_name='items4')
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE , related_name='cartitems4')

    def __str__(self):
        return f"{self.cate_car.name} - {self.cate_car.insurance} - ${self.cate_car.price}"

    def categories_cars_price(self):
        # Get the latest customers_data for the user associated with the cart
        latest_customer_data = self.cart.user.customers_data_set.latest('id')

        # Calculate total days based on pick_up_date and drop_off_date
        total_days = (latest_customer_data.drop_off_date - latest_customer_data.pick_up_date).days + 1

        cate_car_price_per_day=int(self.cate_car.price)
        cate_car_insurance = int(self.cate_car.insurance)
        cate_car_price_for_days = cate_car_price_per_day*total_days
        cate_cars_total_price = cate_car_insurance + cate_car_price_for_days
        return cate_cars_total_price