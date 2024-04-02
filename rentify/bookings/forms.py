from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput
from django.utils import timezone

from rentify.bookings.models import Booking


class CarBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ["bill_to", "booked_car", "start_date", "end_date"]
        widgets = {
            "start_date": forms.DateInput(),
            "end_date": forms.DateInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError("It looks like you are trying to set a start date greater than the end date.")

        return cleaned_data
