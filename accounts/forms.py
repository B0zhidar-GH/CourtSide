from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account, PlayerProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email address')

    class Meta:
        model = Account

        fields = ('username', 'email', 'password1', 'password2')


class PlayerProfileForm(forms.ModelForm):

    class Meta:

        model = PlayerProfile
        exclude = ('user', 'created_at')