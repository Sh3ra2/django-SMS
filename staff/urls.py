from django.urls import path
from . import views


urlpatterns = [
    path('', views.staffviewclass.as_view(), name = "staff-home"),
    path('addstudent/<str:method>/', views.staffviewclass.as_view(), name = "student-add"),
]
