from django.urls import path
from . import views


urlpatterns = [
    path('', views.useradminclass.as_view(), name = "staff-home"),
]
