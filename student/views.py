from django.shortcuts import render
from django.views import View

# Create your views here.

class studentviewclass(View):

    def get(self, request, **kwargs):
        context = {"DATA": "Hello"}
        return render(request=request, template_name="student/home.html", context = context)