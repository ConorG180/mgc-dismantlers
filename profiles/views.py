from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


def profile(request):
  
    return render(request, 'profiles/profile.html')