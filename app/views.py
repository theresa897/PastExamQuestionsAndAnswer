from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from django.contrib import messages
from rest_framework import viewsets
=======
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import FileResponse
from django.contrib import messages
from rest_framework import viewsets
<<<<<<< HEAD
=======
from rest_framework import serializers
<<<<<<< HEAD
>>>>>>> 40cfff371b443bbb9baa776559f6494e9ec36497
=======
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
>>>>>>> be6bf1d917b260178b059697748739e3ed5d3638
from rest_framework.authentication import TokenAuthentication
from .models import School, User, Exam, Answer
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import redirect
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer

=======
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.views import APIView
from .serializers import SchoolSerializer
>>>>>>> be6bf1d917b260178b059697748739e3ed5d3638
=======
from django.shortcuts import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from .serializers import *
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708

class SchoolCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new school
    queryset = School.objects.all(),
    serializer_class = SchoolSerializer

<<<<<<< HEAD
class SchoolList(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)
=======
class SchoolList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708

class SchoolDetail(generics.RetrieveAPIView,):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

<<<<<<< HEAD
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




    
    

    


=======
class SchoolUpdate(generics.UpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
>>>>>>> 40cfff371b443bbb9baa776559f6494e9ec36497

def index(request):

#     # recent_exam = Exam.objects.order_by("created_on")[:5]

    return render(request, template_name="app/index.html")
#     # return HttpResponse("Hello, world")


        
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes= (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
<<<<<<< HEAD
=======
   
>>>>>>> 40cfff371b443bbb9baa776559f6494e9ec36497
        
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=RegisterSerializer

<<<<<<< HEAD
<<<<<<< HEAD
    def get_queryset(self):                                            # added string
        return super().get_queryset().filter(id=self.request.user.id)   # added string
=======
    # def get_queryset(self):                                            # added string
    #     return super().get_queryset().filter(id=self.request.user.id)   # added string
>>>>>>> 40cfff371b443bbb9baa776559f6494e9ec36497

=======
>>>>>>> be6bf1d917b260178b059697748739e3ed5d3638
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

<<<<<<< HEAD
<<<<<<< HEAD
=======
class ExamCreate(generics.ListCreateAPIView):
    # queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    # permission_classes = [IsAuthenticated]
=======
>>>>>>> be6bf1d917b260178b059697748739e3ed5d3638


# Create your views here.
class ExamVotingView(APIView):
    def post(self, request):
        exam_id = request.data.get("id")
        exam = Exam.objects.get(id=exam_id)
        exam.vote += 1
        exam.save()
        data = {
            "user": request.data.get("user"),
            "exam": exam_id,
            "option": "vote"
        }
        exam_serializer = UserExamSerializer(data=data)
        if exam_serializer.is_valid():
            exam_serializer.save()
            return Response(
                {"message": "Successfully upvoted exam"},
                status=status.HTTP_201_CREATED,
            )
        return Response(exam_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExamUploadingView(APIView):
    def post(self, request, *args, **kwargs):
        exam_serializer = ExamSerializer(data=request.data)
        if exam_serializer.is_valid():
            exam_serializer.save()
            return Response(
                {"message": "Exam uploaded successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(
            exam_serializer.errors,
            status=status.HTTP_200_OK,
        )

class ExamDownloadView(APIView):
    def post(self, request):
        exam_id = request.data.get("id")
        try:
            exam = Exam.objects.get(id=exam_id)
        except Exam.DoesNotExist:
            return Response({"message": "Exam not found !"}, status=status.HTTP_400_BAD_REQUEST)

        file_path = exam.file
        data = {
            "user": request.data.get("user"),
            "exam": exam_id,
            "option": "download"
        }
        file_bin = open(file_path, 'rb')
        exam_serializer = UserExamSerializer(data=data)
        return FileResponse(
                file_bin,
                as_attachment=True, filename=f"{exam.title}.pdf"
            )
        # return Response(exam_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamList(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamDetail(generics.RetrieveAPIView,):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamUpdate(generics.RetrieveUpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer        
<<<<<<< HEAD
>>>>>>> 40cfff371b443bbb9baa776559f6494e9ec36497
=======
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
>>>>>>> be6bf1d917b260178b059697748739e3ed5d3638
