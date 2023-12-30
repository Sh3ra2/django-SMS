import time
from django.shortcuts import redirect, get_object_or_404
from useradmin import models

class requstlogmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time =  time.time()

        response = self.get_response(request)
        end_time = time.time()

        elapsed_time = end_time - start_time

        self.log_request_info(request, elapsed_time)

        return response
    
    def log_request_info(self, request, elapsed_time):
        print(f"URL:{request.path}, Method:{request.method}, timetaken: {elapsed_time:.6f} secounds")


class checkusertype:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print("\n\n\n USER IS ", request.user.id)
            
            print("pre rt is ")
            rt = get_object_or_404(models.CustomUser, pk = request.user.id)
            print("rt is ", rt.user_type)
            if rt.user_type == 'User Admin':
                print(request.user, "is ", 'User Admin', rt.user_type)
                # return redirect('useradmin-home')
            elif rt.user_type == 'Staff':
                print(request.user, "is ", 'Staff', rt.user_type)
                # return redirect('staff-home')
                
            elif rt.user_type == 'Student':
                print(request.user, "is ", 'Student', rt.user_type)
                # return redirect('student-home')
            elif rt.user_type == '':
                print(request.user, "is ", 'None')
            else:
                print("Tried to recognise")
           
            
        response = self.get_response(request)
        return response

