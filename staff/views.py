from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.contrib.auth.models import User
from student.models import studentmodel
from student.forms import studentmodelform, studentuserform

# --VIEW-- 
#       --USING MULTI-TEMPLATE--
#                             --APPROACH--

# Create your views here.

class studentuserclass(View):
    template_name = 'staff/studentuseradd.html'

    def get(self, request):
        user_form = studentuserform()
        
        return render(request, self.template_name, {'form': user_form})

    def post(self, request):
        user_form = studentuserform(request.POST)
        
        if user_form.is_valid():
            request.session['user_form_data'] = user_form.cleaned_data
            user_form.save()
            return redirect('addstudent/ADD/')
        
        return render(request, self.template_name, {'form': user_form})


class staffviewclass(View):
    
    def get(self, request, **kwargs):
        
        print("kwargs are: ", kwargs)
        # -- If there is any key word argument
        if kwargs:
            
            # -- Adding new student
            if kwargs["method"] == "ADD":
                user_form_data = request.session.get('user_form_data', {})
                print("user data in session", user_form_data)
                print("username is ", user_form_data["username"])
                # form = studentmodelform(initial= user_form_data)
                form = studentmodelform(initial= {'name': user_form_data['username']})
                print("Form with data is ",form)
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

                user_form_data = request.session.get('user_form_data', {})
                student_form = studentmodelform(request.POST, request.Fiiles)
                if student_form.is_valid():
                    # Combine user data and student data and create instances
                    user = User.objects.create_user(**user_form_data)
                    student = student_form.save(commit=False)
                    student.user = user
                    student.save()
                    # messages.success(request, 'User and Student created successfully.')
                    return redirect('staff-home')
            
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


