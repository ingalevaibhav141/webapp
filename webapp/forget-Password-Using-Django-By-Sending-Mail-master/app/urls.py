from django.urls import path
from .import views
from app import views
from.views import Home1,Add_student,Delete_student,Editstudent
urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.main,name="main"),
    path('changepass/<str:id>/',views.changepassword,name="changepassword"),
    path('forgetpassword/',views.fpass,name='fpass'),

    path('login1/', views.login_view, name='login'),

    path('logout/',views.LogoutPage,name='logout'),

    path('subadmin/',Home1.as_view(),name='home1'),
    path('add-student/', Add_student.as_view(),name='add-student'),
    path('delete-student/',Delete_student.as_view(), name='delete-student'),
    path('edit-student/<int:id>',Editstudent.as_view(),name='edit-student'),
]
 