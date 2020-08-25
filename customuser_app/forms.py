from django import forms
from customuser_app import models

from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models.CustomUserModel
        fields = ['displayname']





