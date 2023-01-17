from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, Make, Model, Part


def render_products(request):
    products = Product.objects.all()
    print(products)
    context = {
        "products": products
    }
    return render(request, 'products/products.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    print(product)
    product.delete()
    return redirect(reverse('products'))