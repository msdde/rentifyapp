from django.db import models
from django.db.models import ForeignKey
from django.utils.text import slugify

from rentify.categories.models import Category


class Cars(models.Model):

    BRAND = (
        ("BMW", "BMW"),
        ("Mercedes", "Mercedes"),
        ("Audi", "Audi"),
    )

    GEARBOX = (
        ("Manual", "Manual"),
        ("Auto", "Auto"),
    )

    brand = models.CharField(
        max_length=20,
        choices=BRAND,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    image = models.ImageField(
        upload_to="cars_image",
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        default=2020,
        null=False,
        blank=False,
    )

    category = ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="cars",
    )

    gearbox = models.CharField(
        max_length=20,
        choices=GEARBOX,
        null=False,
        blank=False,
    )

    price = models.IntegerField(
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.brand}-{self.model}")

        super().save(*args, **kwargs)



