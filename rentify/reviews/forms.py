from django import forms
from rentify.reviews.models import Review


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text",]

