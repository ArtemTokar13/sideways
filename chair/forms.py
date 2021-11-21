from django.contrib.auth.models import User

from chair.admin import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)