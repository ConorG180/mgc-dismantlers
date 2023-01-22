from django.shortcuts import render


# Create your views here.
def render_cart(request):
    return render(request, 'cart/cart.html')