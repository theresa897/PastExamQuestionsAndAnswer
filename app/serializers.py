from rest_framework import serializers
<<<<<<< HEAD
from .models import School, User, Exam, UserExam
=======
<<<<<<< HEAD
from .models import User
=======
from .models import School, User, Exam
>>>>>>> 40cfff371b443bbb9baa776559f6494e9ec36497
>>>>>>> ff796957b686f9d756f43f353f40a988083b6596
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from rest_framework import serializers

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"

    def create(self, validated_data):
        exam = Exam.objects.create(**validated_data)
        exam.save()
        return exam

class UserExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExam
        fields = "__all__"

    def create(self, validated_data):
        user_exam = UserExam.objects.create(**validated_data)
        user_exam.save()
        return user_exam


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        #Add custom claims
        token['name'] = user.username
        return token
    
<<<<<<< HEAD
# class ExamSerializer(serializers.ModelSerializer):
#     school_name = serializers.CharField(source='school.name')
#     files = serializers.ListField(
#         child=serializers.FileField(), write_only=True, required=False
#     )
#     # user_name = serializers.CharField(source='user.name')
=======
<<<<<<< HEAD
=======
class ExamSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name')
    files = serializers.ListField(
        child=serializers.FileField(), write_only=True, required=False
    )
    # user_name = serializers.CharField(source='user.name')
>>>>>>> ff796957b686f9d756f43f353f40a988083b6596

#     class Meta:
#         model = Exam
#         fields=[
#             'id',
#             'content',
#             'title',
#             'subject',
#             'files',
#             'user',
#             'school_name'
#         ]
    
#     def create(self, validated_data):
#         files=validated_data.pop("files", [])
#         exam = Exam.objects.create(**validated_data)
#         return exam

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['pk', 'name', 'location', 'logo']
>>>>>>> 40cfff371b443bbb9baa776559f6494e9ec36497

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True, 'validators': [UniqueValidator(queryset=User.objects.all())]}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from validated_data
        user = User.objects.create_user(**validated_data)
        return user