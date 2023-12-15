from django.db import models
from staff.models import staffmodel
from useradmin.models import gender_choices

# Create your models here.

class_choices = [
    (1,1),
    (2,2),
    (3,3)
]

class studentmodel(models.Model):
    im = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(choices = gender_choices,max_length=50)
    sclass = models.CharField(choices = class_choices, max_length=50)
    age = models.IntegerField()
    Admitted_by = models.ForeignKey(staffmodel, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)