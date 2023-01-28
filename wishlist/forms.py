from django import forms
from products.models import Make, Model, Part, Year

makes = Make.objects.all()
make_choices = tuple([(make.id, make.name) for make in makes])
models = Model.objects.all()
model_choices = tuple([(model.id, model.car_model) for model in models])
parts = Part.objects.all()
part_choices = tuple([(part.id, part.name) for part in parts])
years = Year.objects.all()
year_choices = tuple([(year.id, year.year) for year in years])

class WishlistForm(forms.Form):
    make = forms.ChoiceField(choices=make_choices)
    model = forms.ChoiceField(choices=model_choices)
    part = forms.ChoiceField(choices=part_choices)
    year = forms.ChoiceField(choices=year_choices)
    on_add = forms.BooleanField(label="When part is added", required=False,initial=False)
    on_sale = forms.BooleanField(label="When part is on sale", required=False,initial=False)

    make.widget.attrs.update({'id': 'wishlist_id_make', 'class': 'form-control'})
    model.widget.attrs.update({'id': 'wishlist_id_car_model', 'class': 'form-control'})
    part.widget.attrs.update({'id': 'wishlist_id_part', 'class': 'form-control'})
    year.widget.attrs.update({'id': 'wishlist_id_year', 'class': 'form-control'})
    on_add.widget.attrs.update({'id': 'wishlist_id_on_add'})
    on_sale.widget.attrs.update({'id': 'wishlist_id_on_sale'})