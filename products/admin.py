from django.contrib import admin
from django.apps import apps
from .models import Make, Model, Product, Category, Part

# products_models = apps.get_app_config('products').get_models()

# for model in products_models:
#     admin.site.register(model)


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ("name",)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = [
        "car_model", "make",
        "model_year", "vehicle_category"
    ]
    list_filter = ("make",)
    search_fields = ["car_model"]

@admin.register(Product)
class MakeAdmin(admin.ModelAdmin):
    list_display = ["car_model", "part", "price", "is_sold", "in_a_cart"]
