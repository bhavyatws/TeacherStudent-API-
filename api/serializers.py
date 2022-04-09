from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from django.contrib.auth import get_user_model

from api.models import Assignment
User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # password2=serializers.CharField(_MAX_LENGTH=12)
    class Meta:
        model=User
        fields=['username','first_name','last_name','password','is_teacher']
        extra_kwargs={'password':{'write_only':True},'is_teacher':{'write_only':True}}
    # def validate(self, attrs):
    #     return super().validate(attrs)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','first_name','last_name']

class AssignmentSerializer(serializers.ModelSerializer):
    teacher=UserSerializer(read_only=True)
    class Meta:
        model=Assignment
        fields='__all__'
        # extra_kwargs={'user':{'read_only':True}}
        # exclude=['user',]
