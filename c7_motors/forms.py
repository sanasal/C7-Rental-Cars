from django import forms
from . import models 
from . models import customers_data

class Customers_Data(forms.ModelForm):
    class Meta:
        model = customers_data
        fields = ['cars', 'name', 'email', 'mobile_phone', 'nationality','pick_up_location','drop_off_location', 'pick_up_date' , 'pick_up_time', 'drop_off_date' ,'drop_off_time']