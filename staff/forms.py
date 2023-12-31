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
    password = forms.CharField(widget=forms.PasswordInput)

    
    class Meta:
        model = staffmodel
        fields = "__all__"

    def save(self, commit = True):
        user = super().save(commit =False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        user.is_active = True
        if commit:
            user.save()
        return user