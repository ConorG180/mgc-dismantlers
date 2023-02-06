from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'add-to-wishlist/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),
    path(
        'remove-from-wishlist/<wishlist_id>',
        views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),
]
