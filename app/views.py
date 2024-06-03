from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .models import School, User, Exam, Answer
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.views import APIView
from .serializers import SchoolSerializer

class SchoolCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new school
    queryset = School.objects.all(),
    serializer_class = SchoolSerializer

class SchoolList(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

class SchoolDetail(generics.RetrieveAPIView,):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SchoolUpdate(generics.RetrieveUpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer






def school_list_view(request):
    school_list_view = SchoolList.as_view()
    response = school_list_view(request)
    tests = response.data
    return render(request, 'test.html', {'tests': tests})
        
def index(request):

    return render(request, template_name="app/index.html")




    
    

    


