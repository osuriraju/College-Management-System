from django.urls import path
from . import views


urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('register', views.register),
    path('index', views.index),
    path('addclass', views.addclass),
    path('addfaculty', views.addfaculty),
    path('class/<int:id>', views.viewclass),
    path('class/addstudent/<int:id>', views.addstudent),
    path('class/update/<int:id>',views.updatestudent),
    path('class/delete/<int:id>', views.deletestudent),
    path('update/<int:id>', views.updateclass),
    path('updatefaculty/<int:id>', views.updatefaculty),
]