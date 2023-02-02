from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm
from wishlist.models import Wishlist
from products.models import Make, Model, Year, Part


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_orders = Order.objects.filter(user_profile=user_profile)
    user_wishlist = Wishlist.objects.filter(user=request.user)
    user_profile_form = UserProfileForm(request.POST, instance=user_profile)
    wishlist = []
    for wishlist_item in user_wishlist:
        wishlist_id = wishlist_item.id
        make = Make.objects.get(id=wishlist_item.make_id)
        model = Model.objects.get(id=wishlist_item.car_model_id)
        on_add = wishlist_item.on_add
        on_sale = wishlist_item.on_sale
        try:
            year = Year.objects.get(id=wishlist_item.model_year)
        except Year.DoesNotExist:
            year = "All years"
        try:
            part = Part.objects.get(id=wishlist_item.part_id)
        except Part.DoesNotExist:
            part = "All parts"

        wishlist_product = {
            "wishlist_id": wishlist_id,
            "make": make,
            "model": model,
            "year": year,
            "part": part,
            "on_add": on_add,
            "on_sale": on_sale
        }
        wishlist.append(wishlist_product)

    if request.method == "POST":
        if user_profile_form.is_valid():
            user_profile_form.save()
            # Save email to user
            request.user.email = user_profile_form["email"].value()
            request.user.save()
            return redirect(reverse("profile"))

    else:
        form_data = {
            'email': request.user.email,
            'default_phone_number': user_profile.default_phone_number,
            'default_street_address1': user_profile.default_street_address1,
            'default_street_address2': user_profile.default_street_address2,
            'default_town': user_profile.default_town,
            'default_city': user_profile.default_city,
            'default_county': user_profile.default_county,
            'default_country': user_profile.default_country,
            'default_postcode': user_profile.default_postcode,
        }
        user_profile_form = UserProfileForm(initial=form_data)
        context = {
            "user_profile": user_profile,
            "user_orders": user_orders,
            "user_profile_form": user_profile_form,
            "wishlist": wishlist
        }
        return render(request, 'profiles/profile.html', context)