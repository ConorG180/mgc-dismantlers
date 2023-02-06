from django.contrib import admin
from django.apps import apps

profiles_models = apps.get_app_config('profiles').get_models()

for model in profiles_models:
    admin.site.register(model)
