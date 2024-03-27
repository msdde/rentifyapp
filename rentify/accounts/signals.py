from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RentifyProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_external_profile(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        RentifyProfile.objects.create(user=instance)
