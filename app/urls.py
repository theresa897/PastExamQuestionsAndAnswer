from django.urls import path

from.import views
from .views import *

urlpatterns = [
   
    path('', views.index, name="index"),

    path('school/create/', SchoolCreate.as_view(), name='create-school'),
    path('school/', SchoolList.as_view()),
  
    path('school/<int:pk>/', SchoolDetail.as_view(), name='find-school'),
    path('school/update/<int:pk>/', SchoolUpdate.as_view(), name='update-school'),

    


 



    


    





]
