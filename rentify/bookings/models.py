import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import ForeignKey

from rentify.accounts.models import RentifyProfile
from rentify.cars.models import Cars

UserModel = get_user_model()


class Booking(models.Model):

    bill_to = ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        related_name="booking_profile"
    )

    invoice_date = models.DateField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    booked_car = ForeignKey(
        Cars,
        on_delete=models.CASCADE,
        related_name="booking_car"
    )

    start_date = models.DateField(
        validators=[MinValueValidator(datetime.date.today)],
        blank=True,
        null=True,
    )

    end_date = models.DateField(
        validators=[MinValueValidator(datetime.date.today)],
        blank=True,
        null=True,
    )
