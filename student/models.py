from django.db import models
from staff.models import staffmodel
from useradmin.models import gender_choices

# Create your models here.

class_choices = [
    ("1","1"),
    ("2","2"),
    ("3","3")
]

class studentmodel(models.Model):
    im = models.ImageField( upload_to="student")
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(choices = gender_choices,max_length=50)
    sclass = models.CharField(choices = class_choices, max_length=50)
    age = models.IntegerField()
    admitted_by = models.ForeignKey(staffmodel, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.father_name}"


    

class examsmodel(models.Model):
    session_name = models.CharField(max_length=80)
    subject_name = models.CharField(max_length=80)
    invigilator = models.ManyToManyField(staffmodel)
    taken_by = models.ManyToManyField(studentmodel)

    def __str__(self) -> str:
        return f"{self.session_name}, {self.subject_name}"


class examresultmodel(models.Model):
    exam = models.ForeignKey(examsmodel, on_delete=models.CASCADE)
    student = models.ForeignKey(studentmodel, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()