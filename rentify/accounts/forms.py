from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from rentify.accounts.models import RentifyProfile, RentifyUser

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Please enter a correct %(username)s and password."
    }


class RentifyUserCreationForm(UserCreationForm):
    user = None

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class RentifyChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileEditForm(forms.ModelForm):
    # field to change the email address (username)
    email = forms.EmailField(label='Email')

    class Meta:
        model = RentifyProfile
        fields = ["first_name", "last_name", "phone_number", "profile_picture", "city", "country", "bio"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the current user's email address
        user_email = self.instance.user.email if self.instance.user else None
        # Set initial value for the email field
        self.fields['email'] = forms.EmailField(label='Email', initial=user_email)

    # save changes via form (update user's email address)
    def save(self, commit=True):
        self.instance.user.email = self.cleaned_data['email']
        if commit:
            self.instance.user.save()
        return super().save(commit)
