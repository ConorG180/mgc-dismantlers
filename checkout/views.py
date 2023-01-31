from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings
from cart.context_processors import cart_context_processor
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import stripe

# order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lineitems')
#     product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
#     quantity = models.IntegerField(default=0)
#     lineitem_total


def render_checkout(request):
    if request.method == "POST":
        cart = request.session.get("cart", {})
        user_profile = UserProfile.objects.get(user=request.user)
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town': request.POST['town'],
            'city': request.POST['city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print("ORDER FORM IS VALID")
            order = order_form.save(commit=False)
            order.save()
            order.user_profile = user_profile
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity
                    )
                    order_line_item.save()
                except Product.DoesNotExist():
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database."
                        "Please call us on 0441234567 for assistance.")
                    )
                    order.delete()
                    return redirect(reverse('cart'))
            lineitems = order.lineitems.all()
            for lineitem in lineitems:
                lineitem.product.is_sold = True
                lineitem.product.save()
            del request.session["cart"]
            context = {
                "order": order,
                "lineitems": lineitems
            }
            return render(request, "checkout/checkout-success.html", context)
        else:
            print("SOMETHING WRONG WITH FORM. NOT VALID")
            print(order_form.errors)
    else:
        cart = request.session.get("cart", {})
        grand_total = cart_context_processor(request)["grand_total"]
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        stripe_total = round(100 * grand_total)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        if cart:
            order_form = OrderForm()
            context = {
                "order_form": order_form,
                "stripe_public_key": stripe_public_key,
                "client_secret": intent.client_secret,
            }
            return render(request, 'checkout/checkout.html', context)
        else:
            messages.error(request, "Add something to your cart to access the checkout page")
            return redirect(reverse("products"))
