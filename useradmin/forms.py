from django import forms
from django.contrib.auth.forms import AuthenticationForm
from . import models

class CustomAuthUserForm(AuthenticationForm):
    class Meta:
        model = models.CustomUser
        fields  = ['username', 'password']