from django.core.validators import EmailValidator
from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        required=True,
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
    )

    email = forms.EmailField(
        validators=[EmailValidator()]
    )

    phone = forms.CharField(
        max_length=15,
        required=False,
    )

    subject = forms.CharField(
        max_length=100,
        required=True,
    )

    message = forms.CharField(
        max_length=500,
        required=True,
        widget=forms.Textarea()
    )
