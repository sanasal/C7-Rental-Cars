from django import forms
from . import models 
from . models import customers_data

class Customers_Data(forms.ModelForm):
    class Meta:
        model  = models.customers_data
        fields = ['cars','name' , 'email' ,'mobile_phone', 'nationality', 'price' ,'pick_up_date', 'pick_up_time', 'drop_off_date', 'drop_off_time']
        widgets = {
            'pick_up_date': forms.DateInput(attrs={'type': 'date'}),
            'pick_up_time': forms.TimeInput(attrs={'type': 'time'}),
            'drop_off_date': forms.DateInput(attrs={'type': 'date'}),
            'drop_off_time': forms.TimeInput(attrs={'type': 'time'}),
        } 