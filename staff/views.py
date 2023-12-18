from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from student.models import studentmodel
from student.forms import studentmodelform

# --VIEW-- 
#       --USING MULTI-TEMPLATE--
#                             --APPROACH--

# Create your views here.
class staffviewclass(View):
    
    def get(self, request, **kwargs):
        
        print("kwargs are: ", kwargs)
        # -- If there is any key word argument
        if kwargs:
            
            # -- Adding new student
            if kwargs["method"] == "ADD":
                print("adding new student")
                form = studentmodelform()
                context = {"form": form}
                return render(request= request, template_name="staff/form.html", context = context)
            
            # -- Deleting student
            if kwargs["method"] == "DELETE" and kwargs["pk"]:
                studentmodel.objects.filter(pk = kwargs["pk"]).delete()
                return redirect("staff-home")
            
            # -- Updating student
            if kwargs["method"] == "UPDATE" and kwargs["pk"]:
                user = get_object_or_404(studentmodel, pk = kwargs["pk"])
                form = studentmodelform(instance= user)
                context = {"form": form}
                return render(request=request, template_name="staff/form.html", context=context)
        
        # -- else get data to show on home page
        data =  studentmodel.objects.all()
        page  = request.GET.get('page', 1)
        paginator = Paginator(data, 3)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.numpages)

        context = {"data": data}
        return render(request= request, template_name="staff/home.html", context = context)
    

    def post(self, request, **kwargs):
        # print("I am in Post, kwargs are ", kwargs)
        if kwargs:
            
            # -- form for adding
            if kwargs["method"] == "ADD":
                print("in add of post")
                form = studentmodelform(request.POST, request.FILES)
            
            # -- form to update
            if kwargs["method"] == "UPDATE" and kwargs["pk"]:
                user = get_object_or_404(studentmodel, pk = kwargs["pk"])
                form = studentmodelform(request.POST, request.FILES, instance=user)
        
        # -- form to render 
        else:
            form = studentmodelform(request.POST, request.FILES)
        

        if form.is_valid():
            form.save()
            return redirect("staff-home")
        
        context = {"form": form}
        return render(request= request, template_name="staff/form.html", context = context)
