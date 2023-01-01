"""
Signals for profiles app
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from profiles.models import UserProfile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        print("Profile Created!")
    else:
        # Existing users: just save the profile
        instance.userprofile.save()
        print("Profile Updated!")
