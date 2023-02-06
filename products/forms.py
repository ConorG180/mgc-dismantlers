from django import forms
from .models import Product, Category, Make, Model, Part


class Product_form(forms.ModelForm):

    class Meta:
        make = forms.ModelChoiceField(Make.objects.all())
        model = Product
        fields = '__all__'
        exclude = ('in_a_cart', 'is_sold')

    forms.forms.BaseForm.field_order = ['make', 'car_model']
