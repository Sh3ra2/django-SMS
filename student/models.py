from django.db import models
from staff.models import staffmodel
from django.contrib.auth.models import User
from useradmin.models import gender_choices, CustomUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class_choices = [
    ("1","1"),
    ("2","2"),
    ("3","3")
]
S_Choices = [
    ("Maths", "Maths"),
    ("English", "English"),
    ("English", "Urdu")
]

class studentmodel(CustomUser):
    im = models.ImageField( upload_to="student")
    sclass = models.CharField(choices = class_choices, max_length=50)
    DOB = models.DateField(auto_now=False, auto_now_add=False, default = "2023-9-12")
    admitted_by = models.ForeignKey(staffmodel, on_delete=models.SET_NULL, null = True)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.father_name}"
    
    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


    

class examsmodel(models.Model):
    session_name = models.CharField(max_length=80)
    esubject = models.CharField(choices = S_Choices, max_length=50, default = "English")
    invigilator = models.ForeignKey(staffmodel, on_delete=models.CASCADE, default = 1)
    selected_class = models.CharField(choices = class_choices, max_length=50, default = "2")
    studentforexam = models.ManyToManyField(studentmodel, blank = True)

    def __str__(self) -> str:
        return f"{self.session_name}, {self.esubject}"


class subjectpapermodel(models.Model):
    exam = models.ForeignKey(examsmodel, on_delete=models.CASCADE)
    esubject = models.CharField(choices = S_Choices, max_length=50)
    pstudent = models.ForeignKey(studentmodel, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
