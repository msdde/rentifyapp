from django import forms
from rentify.categories.models import Category


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("Category with this name already exists.")

        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        return description
