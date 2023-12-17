from django import forms
from django.forms import ModelForm
from .models import studentmodel


class studentmodelform(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields = "__all__"