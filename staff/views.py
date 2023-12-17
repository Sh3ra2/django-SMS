from django.shortcuts import render
from django.views import View
from student.models import studentmodel
from student.forms import studentmodelform

# Create your views here.
class staffviewclass(View):
    
    def get(self, request, **kwargs):
        print("kwargs are: ", kwargs)
        if kwargs:
            if kwargs["method"] == "ADD":
                form = studentmodelform()
                context = {"form": form}
                return render(request= request, template_name="staff/home.html", context = context)
        context = {"data": "data here"}
        return render(request= request, template_name="staff/home.html", context = context)