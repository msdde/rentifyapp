from allauth.account.signals import user_signed_up
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RentifyProfile

UserModel = get_user_model()


# signal for creating a profile model for superuser
@receiver(post_save, sender=UserModel)
def create_external_profile(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        RentifyProfile.objects.create(user=instance)


# signal for creating a profile model for Google authenticated users
@receiver(user_signed_up)
def create_profile_for_user(sender, request, user, **kwargs):
    if user.socialaccount_set.filter(provider='google').exists():
        RentifyProfile.objects.create(user=user)
