from django.shortcuts import render, redirect, reverse


# Create your views here.
def render_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = 1
    request.session["cart"] = cart
    return redirect(reverse('products'))