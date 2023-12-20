from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from staff.models import staffmodel
from staff.forms import staffmodelform
from student.forms import examsmodelform
from student.models import examsmodel

# Create your views here.

def index(request):
    return render(request=request, template_name="useradmin/home.html")


class useradminclass(View):
    template_name  = "useradmin/home.html"
    r_list = []

    def get(self, request, pk = None, ftype =  None, tosearch = None, downorder = None,):
        print("to filter and to search :", ftype, tosearch)
        if ftype and tosearch:
            if ftype ==1:
                query = staffmodel.objects.filter(name__icontains = tosearch)
                self.r_list = staffmodel.objects.values_list(pk , flat  = True)
            elif ftype ==2:
                query = staffmodel.objects.filter(father_name__icontains = tosearch)
            elif ftype ==3:
                query = staffmodel.objects.filter(qualification__icontains = tosearch)
            elif ftype ==4:
                query = staffmodel.objects.filter(address__icontains = tosearch)
            elif ftype ==5:
                query = staffmodel.objects.filter(added_by__icontains = tosearch)
        elif pk:
            staffmodel.objects.filter(pk = pk).delete()
        else:
            query = staffmodel.objects.all()
        
        print(query)
        context = {"data": query}
        return render(request= request, template_name=self.template_name, context=context )
    

class staffformview(View):
    template_name = "useradmin/form.html"

    def get(self, request, pk = None):
        if pk:
            user = get_object_or_404(staffmodel, pk = pk)
            form = staffmodelform(instance=user)
        else:
            form =  staffmodelform()
        context = {"form": form}
        return render(request=request, template_name=self.template_name, context=context)
    
    def post(self, request, pk = None):
        print("Form recieved")
        if pk:
            user = get_object_or_404(staffmodel, pk = pk)
            form = staffmodelform(request.POST, request.FILES, instance=user)
        else:
            form =  staffmodelform(request.POST, request.FILES)
        context = {"form": form}
        if form.is_valid():
            print("Form was valid")
            form.save()
            return redirect("useradmin-home")
        else:
            print("Form not valid", form.errors)
        
        return render(request=request, template_name=self.template_name, context=context)
    

class useradmindashboardclass(View):
    template_name = "useradmin/dashboard.html"

    def get(self, request):
        query = staffmodel.objects.all()
        context = {"data": query}
        return render(request = request, template_name=self.template_name, context = context)
    

class examclass(View):
    template_name = "useradmin/examview.html"

    def get(self, request, pk = None):
        print("examclass got ", pk)
        if pk:
            examsmodel.objects.filter(pk = pk).delete()
            return redirect("exam-view")
        query  = examsmodel.objects.all()
        print("query is ", query)
        context = {"data": query}
        print("context is ", context)
        ease = context["data"]
        print("data is here")
        for obj in ease:
            print(obj)
            print(obj.esubject)
            print("manytomany students are", obj.studentforexam)

        return render(request=request, template_name=self.template_name, context = context)


class examnewsetclass(View):
    template_name = "useradmin/form.html"

    def get(self, request, pk = None):

        if pk:
            ins = get_object_or_404(examsmodel, pk = pk)
            form  = examsmodelform(instance=ins)
        else:
            form  = examsmodelform()
        
        context  = {"form": form}
        return render(request=request, template_name=self.template_name, context = context)
    
    def post(self, request, pk = None ):
        
        if pk:
            ins = get_object_or_404(examsmodel, pk= pk)
            form =  examsmodelform(request.POST, instance= ins)
        else:
            form =  examsmodelform(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("exam-view")
        
        context = {"form": form}

        return render(request= request, template_name=self.template_name, context = context)