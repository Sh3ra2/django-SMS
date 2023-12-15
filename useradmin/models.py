from django.db import models

# Create your models here.

gender_choices = [
    ("M", "Male"),
    ("F", "Female"),
    ("O","Other")
]


role_choices = [
    ("P" , "Principle"),
    ("C" , "Clerk"),
    ("O" , "Other")
]

class useradminmodel(models.Model):
    im = models.ImageField(upload_to=None)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(choices = gender_choices, max_length=50)
    role = models.CharField(choices = role_choices,  max_length=50)
    join_date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.role} {self.name}"