import django_filters

from .models import Product, Make, Model


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = [
            "make",
            "car_model",
            "model_year",
            "part",
            "color",
            "grade",
            "fuel"
        ]
