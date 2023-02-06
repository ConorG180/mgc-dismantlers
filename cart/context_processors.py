from products.models import Product
from django.conf import settings


def cart_context_processor(request):
    cart = []
    total = 0
    delivery = settings.STANDARD_DELIVERY_COST
    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    product_count = 0
    test = "TESTING, IS IT WORKING?"

    cart_from_session = request.session.get("cart", {})

    for item_id, quantity in cart_from_session.items():
        product = Product.objects.get(id=item_id)
        total += product.price * quantity
        product_count += quantity
        cart.append({"product": product, "quantity": quantity})

    if total >= free_delivery_threshold:
        delivery = 0

    context = {
        "cart": cart,
        "delivery": delivery,
        "total": total,
        "product_count": product_count,
        "test": test,
        "free_delivery_threshold": free_delivery_threshold,
        "delivery": delivery,
        "grand_total": total + delivery
    }

    return context
