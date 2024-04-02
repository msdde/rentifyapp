from django import forms
from django.utils.text import slugify
from rentify.brands.models import Brand


class CreateBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Brand.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("Brand with this name already exists.")

        return name

    # def clean_slug(self):
    #     slug = self.cleaned_data.get("slug")
    #     if not slug:
    #         name = self.cleaned_data.get("name")
    #         slug = slugify(name)
    #         self.cleaned_data["slug"] = slug
    #     if Brand.objects.filter(slug=slug).exists():
    #         raise forms.ValidationError("Brand with this Slug already exists.")
    #     return slug

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get("name")
    #
    #     if Brand.objects.filter(name=name).exists():
    #         raise forms.ValidationError("Brand with this name already exists.")
    #
    #     # Generate slug only if not provided explicitly
    #     if not cleaned_data.get("slug"):
    #         cleaned_data["slug"] = slugify(name)
    #
    #     return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Ensure slug is generated if not provided explicitly
        if not instance.slug:
            instance.slug = slugify(instance.name)

        if commit:
            instance.save()
        return instance
