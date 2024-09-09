from django.contrib import admin
from .models import  economy_reservation,luxury_reservation,premium_reservation,all_car,Cart , economy_car , premium_car , luxury_car ,news , customers_data


# Register your models here.
admin.site.register(all_car)
admin.site.register(economy_car)
admin.site.register(luxury_car)
admin.site.register(premium_car)
admin.site.register(news)
admin.site.register(Cart)
admin.site.register(customers_data)
admin.site.register(economy_reservation)
admin.site.register(luxury_reservation)
admin.site.register(premium_reservation)