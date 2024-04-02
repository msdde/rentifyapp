from django.contrib.auth import get_user_model
from django.db import models
from rentify.accounts.models import RentifyProfile

UserModel = get_user_model()


class Review(models.Model):
    text = models.TextField(
        max_length=180,
        blank=False,
        null=False,
    )

    author = models.ForeignKey(
        UserModel,
        related_name="user_model",
        on_delete=models.CASCADE

    )

    date = models.DateTimeField(
        auto_now_add=True
    )
