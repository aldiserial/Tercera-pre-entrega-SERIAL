from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    is_staff = forms.BooleanField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "is_staff")