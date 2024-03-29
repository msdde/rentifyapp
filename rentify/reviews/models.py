from django.db import models
from rentify.accounts.models import RentifyProfile


class Review(models.Model):
    text = models.TextField(
        max_length=180,
        blank=False,
        null=False,
    )

    author = models.ForeignKey(
        RentifyProfile,
        related_name="user_profile",
        on_delete=models.CASCADE

    )

    date = models.DateTimeField(
        auto_now_add=True
    )
