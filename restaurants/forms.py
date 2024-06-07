# restaurant/forms.py
from django import forms

class RestaurantForm(forms.Form):
    restaurant_name = forms.CharField(label='Enter Restaurant Name', max_length=100)
