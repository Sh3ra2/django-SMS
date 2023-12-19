from django import forms
from django.forms import ModelForm
from .models import studentmodel, subjectpapermodel, examsmodel


class studentmodelform(forms.ModelForm):

    DOB = forms.DateField(
        label = "DOB",
        required= True,
        widget= forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
    class Meta:
        model = studentmodel
        fields = "__all__"

class examsmodelform(forms.ModelForm):
    class Meta:
        model = examsmodel
        fields = "__all__"

class subjectpapermodelform(forms.ModelForm):
    class Meta:
        model = subjectpapermodel
        fields = "__all__"

        
