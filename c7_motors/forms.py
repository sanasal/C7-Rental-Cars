from django import forms
from . import models 
from . models import customers_data

class Customers_Data(forms.ModelForm):
    class Meta:
        model = customers_data
        fields = ['cars', 'name', 'email', 'mobile_phone', 'nationality', 'price' ]