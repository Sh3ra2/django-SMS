from django.forms import ModelForm
from .models import staffmodel


class staffmodelform(ModelForm):
    class meta:
        model = staffmodel
        fields = "__all__"