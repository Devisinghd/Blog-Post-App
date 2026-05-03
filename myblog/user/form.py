from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    email = forms.EmailField(required=True,label='Email adderess')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm password',
        }