from django.urls import path, include
from . import views

urlpatterns = [
    path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
]