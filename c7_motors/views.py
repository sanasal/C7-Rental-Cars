from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
#CSRF protection
from django.views.decorators.csrf import csrf_protect
from . import forms
from .models import customers_data, all_car, premium_car, categories_reservation , luxury_car , economy_car, Cart, economy_reservation , luxury_reservation, premium_reservation , Booking , Luxury_Booking , Premium_Booking , Categories_Booking
from django.http import HttpResponse
from django.template import Template , Context
from django.http import JsonResponse
import json  
import stripe
from django.conf import settings
from django.views import View
import os
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .delete_expired_date import delete_expired_drop_offs

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_51PaI022KAcGaNCQ2zxyLLDug4axW1o3D0coeBs0LzlcTWi5TljeppgPuaJXU18veEEF4RloZCEd8ThPTGV1jxJUd00TOd9WmIX"

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_ae9d87049f3f9e8712d278b26e9f02b2f9b0dd42f5777d830889d71341aa5aec'

# views.py

import json
import os
import stripe

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.conf import settings


def home(request):
    premiumcars = premium_car.objects.all()
    luxurycars= luxury_car.objects.all()
    economycars = economy_car.objects.all()
    cars = all_car.objects.all()
    context = {
      'premium_car' : premiumcars ,
      'luxury_car' : luxurycars,
      'economy_car' : economycars,
      'all_car': cars,}   
    return render(request, 'home.html' , context )


@login_required(login_url='/log_in/')
def contact_us(request):
    return render(request , 'contact_us.html')

def service(request):
    return render(request , 'service.html')

def feature(request):
    return render(request , 'feature.html')

def about(request):
    return render(request , 'about.html')

def success(request):
    return render(request , 'success.html')

@login_required(login_url='/log_in/')
def economy(request):
    economycars = economy_car.objects.all()
    context = {'economy_car' : economycars } 
    return render(request , 'economy.html' ,context)


@login_required(login_url='/log_in/')
def luxury(request):
    luxurycars = luxury_car.objects.all()
    context = {'luxury_car' : luxurycars  }   
    return render(request , 'luxury.html' , context)
 

@login_required(login_url='/log_in/')
def premium(request):
    premiumcars = premium_car.objects.all()
    context = {'premium_car' : premiumcars }  
    return render(request , 'premium.html' , context)

    

@csrf_protect
#Sign in function
def sign_in(request):
    if request.method =='POST':   
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()              
            #log the user in
            login(request , user)           
            return redirect('c7_motors:home')
    else:           
       form = UserCreationForm()     
    return render(request, 'sign in.html' , {'form' : form})

@csrf_protect
#log in function
def log_in(request):
    if request.method == 'POST' :   
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            if 'next' in request.POST :
                return redirect(request.POST.get('next'))
            else: 
                return redirect ('c7_motors:home')
    else:
        form = AuthenticationForm()
    return render (request , 'log in.html' , {'form':form})


@csrf_protect
#Log out function``
def log_out(request):
    if request.method == 'POST':
        logout(request)   
        return redirect ('c7_motors:home')


@login_required(login_url='/log_in/')
def add_customers_data(request):
    if request.method == 'POST':
        form = forms.Customers_Data(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.writer = request.user
            instance.user = request.user
            instance.save()

            # Create a booking entry to economy cars
            car_name = instance.cars  # Assuming 'cars' field contains the car name
            car = economy_car.objects.filter(name=car_name).first()
            if car:
                Booking.objects.create(
                    car=car,
                    pick_up_date=instance.pick_up_date ,
                    drop_off_date=instance.drop_off_date
                )

            # Create a booking entry to luxury cars
            lux_car_name = instance.cars  # Assuming 'cars' field contains the car name
            lux_car = luxury_car.objects.filter(name=lux_car_name).first()
            if lux_car:
                Luxury_Booking.objects.create(
                    lux_car=lux_car,
                    pick_up_date=instance.pick_up_date ,
                    drop_off_date=instance.drop_off_date
                )

            # Create a booking entry to premium cars
            pre_car_name = instance.cars  # Assuming 'cars' field contains the car name
            pre_car = premium_car.objects.filter(name=pre_car_name).first()
            if pre_car:
                Premium_Booking.objects.create(
                    pre_car=pre_car,
                    pick_up_date=instance.pick_up_date ,
                    drop_off_date=instance.drop_off_date
                )

            # Create a booking entry to categories cars
            cate_car_name = instance.cars  # Assuming 'cars' field contains the car name
            cate_car = all_car.objects.filter(name=cate_car_name).first()
            if cate_car:
                Categories_Booking.objects.create(
                    cate_car=cate_car,
                    pick_up_date=instance.pick_up_date ,
                    drop_off_date=instance.drop_off_date
                )

            # Delete expired bookings
            delete_expired_drop_offs(Booking)
            delete_expired_drop_offs(Luxury_Booking)
            delete_expired_drop_offs(Premium_Booking)
            delete_expired_drop_offs(Categories_Booking)
            
            # Fetch the latest price after saving the form data
            customer_book_price = customers_data.objects.filter(user=request.user).order_by('-id').first()
            if customer_book_price:
                total_price = customer_book_price.total_price()
            else:
                total_price = None
            
            # Return the total price in the JSON response
            return JsonResponse({
                'success': True,
                'total_price': total_price
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False}, status=400)



@login_required(login_url='/log_in/')
def reservation(request):
    cart = None        
    cartitems = []
    cartitems2 = []
    cartitems3 = []
    cartitems4 = []
    customer_book_price = None

    if request.user.is_authenticated:
        try:
            customer_book_price = customers_data.objects.filter(user=request.user).order_by('-id').first()
            if customer_book_price is not None:
                print("Before calling total_price():", customer_book_price.price)
                customer_book_price.total_price()
                print("After calling total_price():", customer_book_price.price)
                customer_book_price.refresh_from_db()  # Refresh the object from the database
                print("After refreshing from database:", customer_book_price.price)
                total_price = customer_book_price.price
            else:
                total_price = None
        except customers_data.DoesNotExist:
            customer_book_price = None
            total_price = None

        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
        cartitems2 = cart.cartitems2.all()
        cartitems3 = cart.cartitems3.all()
        cartitems4 = cart.cartitems4.all()
    
    context = {
        'cart': cart,
        'items': cartitems,
        'items2': cartitems2,
        'items3': cartitems3,
        'items4': cartitems4,
        'customer_book_price': customer_book_price,
        'total_price': total_price
    }

    return render(request, 'reservation.html', context)




def add_to_cart(request):
    data = json.loads(request.body)
    car_id = data["id"]
    car = economy_car.objects.get(id = car_id)

    if request.user.is_authenticated:
        cart , created = Cart.objects.get_or_create(user =request.user,completed = False)
        cartitem , created = economy_reservation.objects.get_or_create(cart = cart,car= car)
        cartitem.save()

    return JsonResponse('Add Item Done' , safe=False)


def add_to_cart2(request):
    data = json.loads(request.body)
    lux_car_id = data["id"]
    lux_car = luxury_car.objects.get(id = lux_car_id)

    if request.user.is_authenticated:
        cart , created = Cart.objects.get_or_create(user =request.user,completed = False)
        cartitems2 , created = luxury_reservation.objects.get_or_create(cart = cart, lux_car = lux_car)
        cartitems2.save() 
    return JsonResponse('Add Item Done' , safe=False)

def add_to_cart3(request):   
    data = json.loads(request.body)
    pre_car_id = data["id"]
    pre_car = premium_car.objects.get(id= pre_car_id)

    if request.user.is_authenticated:
        cart , created = Cart.objects.get_or_create(user =request.user,completed = False)
        cartitems3 , created = premium_reservation.objects.get_or_create(cart = cart,  pre_car  = pre_car)
        cartitems3.save()
    return JsonResponse('Add Item Done' , safe=False)

def add_to_cart4(request):
    data = json.loads(request.body)
    cate_car_id = data["id"]
    cate_car = all_car.objects.get(id = cate_car_id)

    if request.user.is_authenticated:
        cart , created = Cart.objects.get_or_create(user =request.user,completed = False)
        cartitems4 , created = categories_reservation.objects.get_or_create(cart = cart,cate_car= cate_car)
        cartitems4.save()

    return JsonResponse('Add Item Done' , safe=False)


def delete_item(request):
    data = json.loads(request.body)
    car_id = data['id']
    item = economy_car.objects.get(id = car_id)
    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user , completed = False)
        cart_items = economy_reservation.objects.filter(cart=cart , car_id= car_id) 
        cart_items.delete()
    return JsonResponse('Delete Item Done' , safe= False)


def delete_item2(request):
    data = json.loads(request.body)
    car_id = data['id']
    item = luxury_car.objects.get(id = car_id)
    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user , completed = False)
        cart_items = luxury_reservation.objects.filter(cart=cart , lux_car_id = car_id) 
        cart_items.delete()
    return JsonResponse('Delete Item Done' , safe= False)


def delete_item3(request):
    data = json.loads(request.body)
    car_id = data['id']
    item = premium_car.objects.get(id = car_id)
    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user , completed = False)
        cart_items = premium_reservation.objects.filter(cart=cart , pre_car_id = car_id) 
        cart_items.delete()
    return JsonResponse('Delete Item Done' , safe= False)


def delete_item4(request):
    data = json.loads(request.body)
    car_id = data['id']
    item = all_car.objects.get(id = car_id)
    if request.user.is_authenticated:
        cart = Cart.objects.get(user = request.user , completed = False)
        cart_items = categories_reservation.objects.filter(cart=cart , cate_car_id =car_id) 
        cart_items.delete()
    return JsonResponse('Delete Item Done' , safe= False)