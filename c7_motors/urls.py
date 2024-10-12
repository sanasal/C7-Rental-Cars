from django import views
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static      
from django.conf import settings       
from . import views   

app_name='c7_motors'

urlpatterns = [          
    path('' , views.home , name='home'),  
    path('contact/' , views.contact_us , name='contact_us'),
    path('about/' , views.about ,name='about'),
    path('services/' , views.service , name='service' ),
    path('features/' , views.feature , name='feature' ),
    path('economy_cars/' , views.economy , name='economy'),
    path('luxury_cars/' , views.luxury , name='luxury'),
    path('premium_cars/' , views.premium , name='premium'),
    path('log_in/' , views.log_in , name= 'log_in'),
    path('sign_in/' , views.sign_in , name='sign_in'), 
    path('log_out/' , views.log_out , name='log_out'),  
    path('contact_us/' , views.contact_us , name='contact_us'),
    path('Manage_Your_Book/' , views.reservation , name='reservation'),
    path('economy_cars/add_to_cart/' , views.add_to_cart , name='add'),
    path('luxury_cars/add_to_cart2/' , views.add_to_cart2 , name='add2'),
    path('premium_cars/add_to_cart3/' , views.add_to_cart3 , name='add3'),
    path('add_to_cart4/' , views.add_to_cart4 , name='add4'),
    path('Manage_Your_Book/delete/' , views.delete_item),
    path('Manage_Your_Book/delete2/' , views.delete_item2),
    path('Manage_Your_Book/delete3/' , views.delete_item3),
    path('Manage_Your_Book/delete4/' , views.delete_item4 ),
    path('delete/' , views.delete_item),
    path('delete2/' , views.delete_item2),
    path('delete3/' , views.delete_item3),
    path('delete4/' , views.delete_item4),
    path('add_data/' , views.add_customers_data , name = 'add_customers_data'),
    path('C7_payment_success/', views.send_book_data_after_success, name='success'),
    path('cancel/', views.payment_cancel, name='payment-cancel'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session')
]
