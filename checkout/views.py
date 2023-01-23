from django.shortcuts import render
from .forms import OrderForm


def render_checkout(request):
    order_form = OrderForm()
    context = {
        "order_form": order_form
    }
    print(order_form)
    return render(request, 'checkout/checkout.html', context)
