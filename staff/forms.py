from django import forms
from django.forms import ModelForm, SelectDateWidget
from .models import staffmodel

class staffmodelform(forms.ModelForm):
    join_date = forms.DateField(
        label="join_date",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
    class Meta:
        model = staffmodel
        fields = "__all__"