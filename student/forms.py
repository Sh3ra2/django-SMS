from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import studentmodel, subjectpapermodel, examsmodel


class studentuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "password1", "password2"]



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


    def save(self, commit=True):
        # Access form data before saving
        selected_class = self.cleaned_data.get('selected_class')

        # Your logic to get students based on the selected class
        selected_students = studentmodel.objects.filter(sclass=selected_class)

        # Save the form and get the instance
        instance = super().save(commit)

        # Add selected students to the many-to-many field
        instance.studentforexam.set(selected_students)

        if commit:
            instance.save()

        return instance


class subjectpapermodelform(forms.ModelForm):
    class Meta:
        model = subjectpapermodel
        fields = "__all__"

        
