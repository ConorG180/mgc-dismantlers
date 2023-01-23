from django.shortcuts import render, redirect, reverse
from products.models import Product


# Create your views here.
def render_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    added_product = Product.objects.get(id=product_id)
    added_product.in_a_cart = True
    added_product.save()
    print(f"Here is the added product {added_product} {added_product.color} {added_product.grade}")
    cart = request.session.get('cart', {})
    cart[product_id] = 1
    request.session["cart"] = cart
    return redirect(reverse('products'))


def remove_from_cart(request, product_id):
    removed_product = Product.objects.get(id=product_id)
    removed_product.in_a_cart = False
    removed_product.save()
    print(f"Here is the removed product {removed_product} {removed_product.color} {removed_product.grade}")
    cart = request.session.get('cart', {})
    del cart[product_id]
    request.session["cart"] = cart
    return redirect(reverse('cart'))
