from django.urls import path
from cart import views
urlpatterns = [
    path('', views.render_cart, name='cart'),
]