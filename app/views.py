from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from .models import School, User, Exam, Answer
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.shortcuts import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from .serializers import SchoolSerializer,ExamSerializer,RegisterSerializer, MyTokenObtainPairSerializer

class SchoolCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new school
    queryset = School.objects.all(),
    serializer_class = SchoolSerializer

class SchoolList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetail(generics.RetrieveAPIView,):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolUpdate(generics.UpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

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

    # def get_queryset(self):                                            # added string
    #     return super().get_queryset().filter(id=self.request.user.id)   # added string

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ExamCreate(generics.ListCreateAPIView):
    # queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        school_id = self.kwargs.get("id")
        return School.objects.filter(id=school_id).order_by("created_on")

    def perform_create(self, serializer):
        school_id = serializer.validated_data["school"]
        try:
            school = School.objects.get(name=school_id)
        except School.DoesNotExist:
            raise serializer.ValidationError({"school":"School not found"})
        
        serializer.save(school_name=school.id, user=self.request.user)


class ExamList(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamDetail(generics.RetrieveAPIView,):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamUpdate(generics.RetrieveUpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer        