from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address', required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
                               required=True)
