from django import forms
from rentify.cars.models import Cars


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"


