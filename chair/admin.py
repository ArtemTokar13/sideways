from django.contrib import admin

from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

from chair.models import ChairModel


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

    def clean_password2(self):
        """Check username and passwords"""
        print('WE ARE HERE')
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print(type(username))
        if re.match(r'.*[A-Z|~]+.*', username):
            raise ValidationError('Username can`t contain uppercase simbol or tild (~)')
        if not re.match(r'[\W\w]+@[\W\w]+', username):
            raise ValidationError('Username should be in style "[especialidad]@[nombre del hospital]"')
        if re.match(r'.*[A-Z|~]+.*', password1):
            raise ValidationError('Password can`t contain uppercase simbol or tild (~)')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords didn`t match')
        return password2

    def save(self, commit=True):
        """Saving password in hash format"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


admin.site.register(ChairModel)
