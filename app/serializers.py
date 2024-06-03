


from rest_framework import serializers
from .models import School, User, Exam

from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

    


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['pk', 'name', 'location', 'logo']

    
    