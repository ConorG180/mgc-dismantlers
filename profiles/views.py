from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_orders = Order.objects.filter(user_profile=user_profile)
    user_profile_form = UserProfileForm(request.POST, instance=user_profile)

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
        }
        return render(request, 'profiles/profile.html', context)