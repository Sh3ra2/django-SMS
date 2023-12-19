from django.contrib import admin
from .models import studentmodel, examsmodel, subjectpapermodel
# Register your models here.

admin.site.register(studentmodel)
admin.site.register(examsmodel)
admin.site.register(subjectpapermodel)
