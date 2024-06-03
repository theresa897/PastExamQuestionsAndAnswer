from django.urls import path
<<<<<<< HEAD

=======
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
from.import views
from .views import *

urlpatterns = [
<<<<<<< HEAD
   
    path('', views.index, name="index"),

    path('school/create/', SchoolCreate.as_view(), name='create-school'),
    path('school/', SchoolList.as_view()),
  
    path('school/<int:pk>/', SchoolDetail.as_view(), name='find-school'),
    path('school/update/<int:pk>/', SchoolUpdate.as_view(), name='update-school'),

    


 



    


    





]
=======
    path('', views.index, name="index"),
    path('exam/create', ExamUploadingView.as_view(), name='create-exam'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', Register.as_view(), name="register"),
    path('school/create/', SchoolCreate.as_view(), name='create-school'),
    path('school/', SchoolList.as_view()),
    path('user/', UserList.as_view()),
    path('school/<int:pk>/', SchoolDetail.as_view(), name='find-school'),
    path('school/update/<int:pk>/', SchoolUpdate.as_view(), name='update-school'),
    path('exam/', ExamList.as_view()),
    path('exam/<int:pk>/', ExamDetail.as_view(), name='find-school'),
    path('exam/update/<int:pk>/', ExamUpdate.as_view(), name='update-school'),
]
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
