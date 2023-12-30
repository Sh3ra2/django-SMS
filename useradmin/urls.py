from django.urls import path
from . import views


urlpatterns = [
    # -- staff management urls
    path('', views.useradminclass.as_view(), name = "useradmin-home"),
    path('delete/<int:pk>/', views.useradminclass.as_view(), name = "useradmin-home"),
    path('filter/<int:ftype>/<str:tosearch>/', views.useradminclass.as_view(), name = "useradmin-home"),
    path('orderdesc/<int:downorder>/', views.useradminclass.as_view(), name = "useradmin-home"),
    path('getstaff', views.staffformview.as_view(), name = "useradmin-getstaff"),
    path('update/<int:pk>/', views.staffformview.as_view(), name = "useradmin-getstaff"),
    # -- dashboard urls
    path("dashboard/", views.useradmindashboardclass.as_view(), name = "useradmin-dashboard"),
    # -- exam urls
    path('viewexam', views.examclass.as_view(), name="exam-view"),
    path('newexam', views.examnewsetclass.as_view(), name="exam-new"),
    path('deleteexam/<int:pk>/', views.examclass.as_view(), name="exam-delete"),
    path('updateexam/<int:pk>/', views.examnewsetclass.as_view(), name="exam-update"),
]
