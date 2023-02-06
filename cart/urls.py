from django.urls import path
from cart import views
urlpatterns = [
    path('', views.render_cart, name='cart'),
    path('add-to-cart/<product_id>', views.add_to_cart, name='add_to_cart'),
    path(
        'remove-from-cart/<product_id>',
        views.remove_from_cart,
        name='remove_from_cart'),
]
