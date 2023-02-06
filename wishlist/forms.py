from django import forms
from products.models import Make, Model, Part, Year

# Makes
makes = Make.objects.all()
make_choices = [(make.id, make.name) for make in makes]
# Car Models
models = Model.objects.all()
empty_model_choice = (0, "----------")
model_choices = [(model.id, model.car_model) for model in models]
model_choices.insert(0, empty_model_choice)
# Parts
parts = Part.objects.all()
empty_part_choice = (0, "All parts")
part_choices = [(part.id, part.name) for part in parts]
part_choices.insert(0, empty_part_choice)
# Years
years = Year.objects.all()
empty_year_choice = (0, "All years")
year_choices = [(year.id, year.year) for year in years]
year_choices.insert(0, empty_year_choice)


class WishlistForm(forms.Form):
    make = forms.ChoiceField(choices=make_choices)
    model = forms.ChoiceField(choices=model_choices)
    part = forms.ChoiceField(choices=part_choices)
    year = forms.ChoiceField(choices=year_choices)
    on_add = forms.BooleanField(
        label="When added",
        required=False,
        initial=False
    )
    on_sale = forms.BooleanField(
        label="When on sale",
        required=False,
        initial=False
        )

    make.widget.attrs.update(
        {
            'id': 'wishlist_id_make',
            'class': 'form-control'
        }
    )
    model.widget.attrs.update(
        {
            'id': 'wishlist_id_car_model',
            'class': 'form-control'
        }
    )
    part.widget.attrs.update(
        {
            'id': 'wishlist_id_part',
            'class': 'form-control'
        }
    )
    year.widget.attrs.update(
        {
            'id': 'wishlist_id_year',
            'class': 'form-control'
        }
    )
    on_add.widget.attrs.update({'id': 'wishlist_id_on_add'})
    on_sale.widget.attrs.update({'id': 'wishlist_id_on_sale'})
