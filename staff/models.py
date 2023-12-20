from django.db import models
from django.contrib.auth.models import AbstractUser
from useradmin.models import useradminmodel
from useradmin.models import gender_choices

# Create your models here.


class staffmodel(models.Model):
    im = models.ImageField(upload_to="staff")
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(choices = gender_choices, max_length=50)
    qualification = models.CharField(max_length=50)
    added_by = models.ForeignKey(useradminmodel, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    join_date = models.DateField(auto_now=False, auto_now_add=False)
    till = models.DateField(auto_now=False, auto_now_add=False, null = True, blank = True)

    class Meta:
        default_related_name = 'staff_user'  # Set a unique related_name


    def __str__(self) -> str:
        return f"{self.name}, {self.qualification}"
