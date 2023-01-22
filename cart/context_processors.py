from products.models import Product


def cart_context_processor(request):
    cart = []
    total = 0
    product_count = 0
    test = "TESTING, IS IT WORKING?"

    cart_from_session = request.session.get("cart", {})

    for item_id, quantity in cart_from_session.items():
        product = Product.objects.get(id=item_id)
        total += product.price * quantity
        product_count += quantity
        cart.append({"item_id": item_id, "quantity": quantity, "product": product})

    context = {
        "cart": cart,
        "total": total,
        "product_count": product_count,
        "test": test
    }

    return context
