from django.urls import path
from.import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', Register.as_view(), name="register"),
    path('user/', UserList.as_view()),
]