from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'city', 'state', 'zipcode', 'phone')
        help_texts = {
            'username': 'Please enter your username.',
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ( 'first_name', 'last_name', 'email', 'address', 'city', 'state', 'zipcode', 'phone')



