from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.render_products, name='products'),
    path(
        "delete-product/<product_id>/",
        views.delete_product,
        name="delete_product"
    ),
    path(
        "edit-product/<product_id>/",
        views.edit_product,
        name="edit_product"
    ),
    path('ajax/load-models/', views.load_models, name='ajax_load_car_models'),  # AJAX
]