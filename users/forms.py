from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EmailSignUp(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

class EmailChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['email', ]
