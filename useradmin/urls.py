from django.urls import path
from . import views


urlpatterns = [
    path('', views.useradminclass.as_view(), name = "useradmin-home"),
    path('delete/<int:pk>/', views.useradminclass.as_view(), name = "useradmin-home"),
    path('filter/<int:ftype>/<str:tosearch>/', views.useradminclass.as_view(), name = "useradmin-home"),
    path('orderdesc/<int:downorder>/', views.useradminclass.as_view(), name = "useradmin-home"),
    path('getstaff', views.staffformview.as_view(), name = "useradmin-getstaff"),
    path('update/<int:pk>/', views.staffformview.as_view(), name = "useradmin-getstaff")
]
