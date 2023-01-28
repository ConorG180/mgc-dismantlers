from django.contrib import admin
from .models import Wishlist
# Register your models here.

@admin.register(Wishlist)
class MakeAdmin(admin.ModelAdmin):
    list_display = ["make_id", "car_model_id", "part_id", "model_year", "on_add", "on_sale"]
