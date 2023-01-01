from django.contrib import admin
from django.apps import apps

products_models = apps.get_app_config('products').get_models()

for model in products_models:
    admin.site.register(model)