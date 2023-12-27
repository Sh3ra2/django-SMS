from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from useradmin.models import useradminmodel
from useradmin.models import CustomUser
from useradmin.models import gender_choices
from django.utils.translation import gettext_lazy as _
# Create your models here.


class staffmodel(CustomUser):
    im = models.ImageField(upload_to="staff")
    qualification = models.CharField(max_length=50)
    added_by = models.ForeignKey(useradminmodel, on_delete=models.CASCADE, default= 1)
    join_date = models.DateField(auto_now=False, auto_now_add=False)
    till = models.DateField(auto_now=False, auto_now_add=False, null = True, blank = True)

    def __str__(self) -> str:
        return f"{self.name}, {self.qualification}"
    
    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff Members')