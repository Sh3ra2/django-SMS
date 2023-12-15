from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from staff.models import staffmodel
from staff.forms import staffmodelform

# Create your views here.

def index(request):
    return render(request=request, template_name="useradmin/home.html")


class useradminclass(View):
    template_name  = "useradmin/home.html"

    def get(self, request):

        query = staffmodel.objects.all()
        print(query)
        context = {"data": query}
        return render(request= request, template_name=self.template_name, context=context )