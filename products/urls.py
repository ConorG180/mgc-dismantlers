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
    path(
        "add-product/",
        views.add_product,
        name="add_product"
    ),
    path(
        "search-product/",
        views.search_product,
        name="search_product"
    ),
    # A
    # Ajax path to load car_models
    path('ajax/load-models/', views.load_models, name='ajax_load_car_models'),  # AJAX
]