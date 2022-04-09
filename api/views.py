from email import header
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
import json
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize
from api.serializers import *
from django.contrib.auth import get_user_model
User = get_user_model()
from api.permissions import TeacherOnly

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer
    
    serializer_action_classes={
        'list':RegisterSerializer}
 
    def get_serializer_class(self):
        print(self.action)
        try:
            return self.serializer_action_classes[self.action]
            
        except:
            return super().get_serializer_class()
  

    

class AssignmentView(viewsets.ModelViewSet):
    def get_queryset(self):
        return Assignment.objects.all()
    serializer_class=AssignmentSerializer
    permission_classes=[TeacherOnly,]

    def perform_create(self, serializer):
        return serializer.save(teacher=self.request.user)
   
 
    
   
        
       
