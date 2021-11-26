from django import forms
from django.contrib.auth.models import User

from chair.admin import UserCreationForm
from chair.models import ChairModel


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)



class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Usario', 'style':
                                   'width: 300px;'
                                   'height: 50px;'
                                   'border-radius: 15px;'
                                   'font-size: 22px;'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'style':
                                   'width: 300px;'
                                   'height: 50px;'
                                   'border-radius: 15px;'
                                   'font-size: 22px;'}))
    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.Textarea(attrs={'placeholder': 'Usario', 'style': 'width: 300px;'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'style': 'width: 300px;'})
        }