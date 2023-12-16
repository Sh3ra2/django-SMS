from django.db import models
from useradmin.models import useradminmodel
from useradmin.models import gender_choices

# Create your models here.


class staffmodel(models.Model):
    im = models.ImageField(upload_to="staff", height_field=None, width_field=None, max_length=None)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(choices = gender_choices, max_length=50)
    qualification = models.CharField(max_length=50)
    added_by = models.ForeignKey(useradminmodel, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    join_date = models.DateField(auto_now=False, auto_now_add=False)
    till = models.DateField(auto_now=False, auto_now_add=False, null = True, blank = True)
