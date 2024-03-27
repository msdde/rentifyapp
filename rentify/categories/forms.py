from django import forms
from rentify.categories.models import Category


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError("Category with this name already exists.")

        # description = self.cleaned_data.get("description")
        # if Category.objects.filter(description=description).exists():
        #     raise forms.ValidationError("Category with this name already exists.")

        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        # max_length = Category._meta.get_field("description").max_length
        # if len(description) > max_length:
        #     raise forms.ValidationError(f"Description must be {max_length} characters or fewer.")
        return description
