from django.contrib import admin
from .models import studentmodel, examsmodel, examresultmodel
# Register your models here.

admin.site.register(studentmodel)
admin.site.register(examsmodel)
admin.site.register(examresultmodel)
