from django.db import models


class Brand(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
    )

    logo = models.ImageField(
        upload_to="brands_logo/",
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=True
    )

    # def save(self, *args, **kwargs):
    #     # super().save(*args, **kwargs)
    #
    #     if not self.slug:
    #         self.slug = slugify(f"{self.name}")
    #
    #     super().save(*args, **kwargs)
