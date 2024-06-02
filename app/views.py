from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .models import School, User, Exam, Answer
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.shortcuts import redirect
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer


def index(request):

#     # recent_exam = Exam.objects.order_by("created_on")[:5]

    return render(request, template_name="app/index.html")
#     # return HttpResponse("Hello, world")


        
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes= (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
        
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=RegisterSerializer

    def get_queryset(self):                                            # added string
        return super().get_queryset().filter(id=self.request.user.id)   # added string

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

