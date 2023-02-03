from django import forms
from .models import Product, Category, Make, Model, Part


class Product_form(forms.ModelForm):
    # list_of_makes = Make.objects.all()
    # make = forms.ModelChoiceField(queryset=list_of_makes, to_field_name="name")
    # make = forms.ModelChoiceField(Make.objects.order_by("name"))

    class Meta:
        make = forms.ModelChoiceField(Make.objects.all())
        model = Product
        fields = '__all__'

    forms.forms.BaseForm.field_order = ['make', 'car_model']

    # THIS ALLOWS  MODELS TO COME UP BLANK, BUT CURRENTLY CAUSING ERRORS WHEN SUBMITTING.
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['car_model'].queryset = Model.objects.none()
