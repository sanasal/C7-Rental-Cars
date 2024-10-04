from django.contrib import admin
from .models import  economy_reservation,luxury_reservation,premium_reservation,all_car,Cart , economy_car , premium_car , luxury_car, customers_data , Booking ,Categories_Booking , Luxury_Booking , Premium_Booking


# Register your models here.
admin.site.register(all_car)
admin.site.register(economy_car)
admin.site.register(luxury_car)
admin.site.register(premium_car)
admin.site.register(Cart)
admin.site.register(customers_data)
admin.site.register(economy_reservation)
admin.site.register(luxury_reservation)
admin.site.register(premium_reservation)
admin.site.register(Categories_Booking)
admin.site.register(Booking)
admin.site.register(Premium_Booking)
admin.site.register(Luxury_Booking)