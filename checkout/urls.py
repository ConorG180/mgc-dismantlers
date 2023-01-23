from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.render_checkout, name='checkout'),
    ] 
