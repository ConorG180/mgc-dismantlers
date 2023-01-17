from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Make, Model, Part


def render_products(request):
    products = Product.objects.all()
    print(products)
    context = {
        "products": products
    }
    return render(request, 'products/products.html', context)