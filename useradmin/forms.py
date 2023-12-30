from django import forms
from useradmin import models

class UserAdminModelForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.useradminmodel
        fields = '__all__'

    def save(self, commit = True):
        user = super().save(commit =False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        user.is_active = False
        if commit:
            user.save()
        return user