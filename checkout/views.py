from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.contrib import messages


def render_checkout(request):
    cart = request.session.get("cart", {})
    if cart:
        order_form = OrderForm()
        context = {
            "order_form": order_form
        }
        print(order_form)
        return render(request, 'checkout/checkout.html', context)
    else:
        messages.error(request, "Add something to your cart to access the checkout page")
        return redirect(reverse("products"))
