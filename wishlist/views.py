from django.shortcuts import render, redirect, reverse
from .models import Wishlist
from .forms import WishlistForm


def add_to_wishlist(request):
    if request.method == "POST":
        wishlist_form = WishlistForm(request.POST)
        if wishlist_form.is_valid():
            wishlist_part = Wishlist(
                make_id=request.POST["make"],
                car_model_id=request.POST["model"],
                part_id=request.POST["part"],
                model_year=request.POST["year"],
                on_add="on_add" in request.POST or False,
                on_sale="on_sale" in request.POST or False
            )
            wishlist_part.save()
            wishlist_part.user.add(request.user),
            return redirect(reverse('homepage'))
        else:
            return redirect(reverse('homepage'))


def remove_from_wishlist(request, wishlist_id):
    wishlist_item = Wishlist.objects.get(pk=wishlist_id)
    wishlist_item.delete()
    return redirect(reverse('profile'))