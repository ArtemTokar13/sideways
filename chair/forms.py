from django import forms
from django.contrib.auth.models import User

from chair.admin import UserCreationForm
from chair.models import ChairModel


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


class ChairForm(forms.ModelForm):
    class Meta:
        model = ChairModel
        fields = ('destino',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
