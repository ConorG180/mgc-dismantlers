from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def render_cart(request):
    return render(request, 'cart/cart.html')

@login_required
def add_to_cart(request, product_id):
    added_product = Product.objects.get(id=product_id)
    added_product.in_a_cart = True
    added_product.save()
    cart = request.session.get('cart', {})
    cart[product_id] = 1
    request.session["cart"] = cart
    messages.success(request, f"Added {added_product.create_card_title()} to cart")
    return redirect(reverse('products'))

@login_required
def remove_from_cart(request, product_id):
    removed_product = Product.objects.get(id=product_id)
    removed_product.in_a_cart = False
    removed_product.save()
    cart = request.session.get('cart', {})
    try:
        del cart[product_id]
    except Product.DoesNotExist():
        messages.error(request, f"Oops! An error occured while removing {removed_product.create_card_title()} from cart")
        return redirect(reverse('cart'))
    request.session["cart"] = cart
    messages.success(request, f"Deleted {removed_product.create_card_title()} from cart")
    return redirect(reverse('cart'))
