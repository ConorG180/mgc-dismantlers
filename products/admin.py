from django.contrib import admin
from django.apps import apps
from .models import Make, Model, Product, Category, Part, Color, Year


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ("name",)


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = [
        "car_model", "make",
        "vehicle_category"
    ]
    list_filter = ("make",)
    search_fields = ["car_model"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "car_model",
        "part",
        "image",
        "price",
        "is_sold",
        "in_a_cart"
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "friendly_name"]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["color"]


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ["year"]


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ["name"]
