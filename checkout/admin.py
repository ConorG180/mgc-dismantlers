from django.contrib import admin
from django.apps import apps

checkout_models = apps.get_app_config('checkout').get_models()

for model in checkout_models:
    admin.site.register(model)