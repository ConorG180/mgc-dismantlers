from django.shortcuts import render, redirect, reverse
from .models import Wishlist
from .forms import WishlistForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
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
            messages.success(request, f"Successfully added entry to wishlist!")
            return redirect(reverse('homepage'))
        else:
            for error, errorvalue in wishlist_form.errors.items():
                for erroritem in errorvalue:
                    erroritem = erroritem.replace("&", "&amp;")
                messages.error(request, f"Failed to add entry to wishlist. Problem with {error} field: {erroritem}")
            return redirect(reverse('homepage'))

@login_required
def remove_from_wishlist(request, wishlist_id):
    try:
        wishlist_item = Wishlist.objects.get(pk=wishlist_id)
        wishlist_item.delete()
    except Wishlist.DoesNotExist:
        messages.error(request, f"Oops! An error occured while removing this entry from your wishlist!")
        return redirect(reverse('profile'))
    messages.success(request, f"Successfully removed entry from wishlist!")
    return redirect(reverse('profile'))



    