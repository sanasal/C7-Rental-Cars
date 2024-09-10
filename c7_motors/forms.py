from django import forms
from . import models 
from . models import customers_data

class Customers_Data(forms.ModelForm):
    class Meta:
        model  = models.customers_data
        fields = ['cars','name' , 'email' ,'mobile_phone', 'nationality' , 'start_data' , 'end_data']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }