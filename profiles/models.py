from django.db import models
from django.contrib.auth.models import User
# from django_countries.fields import CountryField


# Add in select menu for countries later
class UserProfile(models.Model):
    """
    A user profile model for account holders
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town = models.CharField(max_length=50)
    default_city = models.CharField(max_length=50, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=60)

    def __str__(self):
        return self.user.username