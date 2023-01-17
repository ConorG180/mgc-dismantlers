from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.render_products, name='products'),
    path(
        "delete-product/<product_id>",
        views.delete_product,
        name="delete_product"
    ),
]