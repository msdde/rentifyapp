from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rentify.accounts.managers import RentifyUserManager


# custom auth user
class RentifyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email"),
        unique=True,
        error_messages={
            "unique": _("This email already exists! Please choose another one."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = RentifyUserManager()

    def __str__(self):
        return self.email.split('@')[0]


# regular user profile
class RentifyProfile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        null=True,
        blank=True,
    )

    city = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    country = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )

    bio = models.TextField(
        max_length=200,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        RentifyUser,
        primary_key=True,
        related_name="user_profile",
        on_delete=models.CASCADE,
    )

