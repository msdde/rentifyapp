from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=True,
    )

    description = models.TextField(
        max_length=150,
        blank=False,
        null=False,
    )

    image = models.ImageField(
        upload_to="categories/"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}")

        super().save(*args, **kwargs)


