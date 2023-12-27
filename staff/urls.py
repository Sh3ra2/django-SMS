from django.urls import path
from . import views


urlpatterns = [
    path('', views.staffviewclass.as_view(), name = "staff-home"),
    path('addstudent/<str:method>/', views.staffviewclass.as_view(), name = "student-add"),
    path('updatestudent/<str:method>/<int:pk>/', views.staffviewclass.as_view(), name = "student-update"),
    path('deletestudent/<str:method>/<int:pk>/', views.staffviewclass.as_view(), name = "student-delete"),
    path('studentuseradd', views.studentuserclass.as_view(), name = "studentuser-add"),

]
