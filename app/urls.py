from django.urls import path
<<<<<<< HEAD

=======
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
from.import views
from .views import *

urlpatterns = [
<<<<<<< HEAD
   
    path('', views.index, name="index"),
<<<<<<< HEAD
<<<<<<< HEAD
    path('exam/create', ExamUploadingView.as_view(), name='create-exam'),
=======
=======
>>>>>>> 75858e5c432949463c59dd57c83ca4869457091e
<<<<<<< HEAD
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', Register.as_view(), name="register"),
    path('user/', UserList.as_view()),
=======
    path('exam/create', ExamCreate.as_view(), name='create-exam'),
<<<<<<< HEAD
>>>>>>> ff796957b686f9d756f43f353f40a988083b6596
=======
=======

    path('school/create/', SchoolCreate.as_view(), name='create-school'),
    path('school/', SchoolList.as_view()),
  
    path('school/<int:pk>/', SchoolDetail.as_view(), name='find-school'),
    path('school/update/<int:pk>/', SchoolUpdate.as_view(), name='update-school'),

    


 



    


    





]
=======
    path('', views.index, name="index"),
    path('exam/create', ExamUploadingView.as_view(), name='create-exam'),
>>>>>>> be6bf1d917b260178b059697748739e3ed5d3638
>>>>>>> 75858e5c432949463c59dd57c83ca4869457091e
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
<<<<<<< HEAD
>>>>>>> 40cfff371b443bbb9baa776559f6494e9ec36497
]
=======
]
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
>>>>>>> be6bf1d917b260178b059697748739e3ed5d3638
