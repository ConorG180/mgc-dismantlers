from products.models import Product


def cart_context_processor(request):
    cart = []
    total = 0
    delivery = 10
    product_count = 0
    test = "TESTING, IS IT WORKING?"

    cart_from_session = request.session.get("cart", {})

    for item_id, quantity in cart_from_session.items():
        product = Product.objects.get(id=item_id)
        total += product.price * quantity
        product_count += quantity
        cart.append({"product": product, "quantity": quantity})

    context = {
        "cart": cart,
        "delivery": delivery,
        "total": total,
        "product_count": product_count,
        "test": test,
        "grand_total": total + delivery
    }

    return context
