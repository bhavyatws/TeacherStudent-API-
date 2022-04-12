
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from api.serializers import *
from django.contrib.auth import get_user_model
User = get_user_model()
from api.permissions import TeacherOnly,OwnerOnly

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
    
    def perform_create(self, serializer):
        instance=serializer.save()
        instance.set_password(instance.password)
        instance.save()
      
  

    

class AssignmentView(viewsets.ModelViewSet):
    def get_queryset(self):
        return Assignment.objects.all()
    serializer_class=AssignmentSerializer
    permission_classes=[TeacherOnly,]
    # def get_serializer_class(self):
    #     if self.request.method == 'PUT':
    #         return AssignedSerializer
    #     return self.serializer_class

    def perform_create(self, serializer):
        return serializer.save(teacher=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(teacher=self.request.user)

    #assign task to student
    @action(detail=True, methods=['patch'],permission_classes=[TeacherOnly])
    def add_student(self, request, pk=None):
        print(pk)
        serializer = AssignmentSerializer(data=request.data)
        student_id=request.data['student']
        print(student_id)
        if serializer.is_valid():
            student_obj=User.objects.get(id=student_id)
            asssignment=Assignment.objects.get(id=pk)
            asssignment.student.add(student_obj)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            # serializer.save()
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #remove assign task,assigned to student
    @action(detail=True, methods=[ 'delete'],permission_classes=[TeacherOnly])
    def remove_student(self, request, pk=None):
        print(pk)
        serializer = AssignmentSerializer(data=request.data)
        student_id=request.data['student']#getting from form_data or json
        print(student_id)
        if serializer.is_valid():
            student_obj=User.objects.get(id=student_id)
            asssignment=Assignment.objects.get(id=pk)
            asssignment.student.remove(student_obj)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            # serializer.save()
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentView(viewsets.ModelViewSet):
    def get_queryset(self):
        id=self.request.GET.get('id')
        if id:
            return Comment.objects.filter(id=id)
        else:
            return Comment.objects
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticated,OwnerOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)
    
    @action(detail=True, methods=[ 'PATCH'],permission_classes=[IsAuthenticated])
    def add_comment(self, request, pk=None):
        print("pk",pk)
        serializer = CommentSerializer(data=request.data)
        assignment_id=request.data['assignment']#getting from form_data or json
        print(assignment_id)
        
        if serializer.is_valid():
            for i in assignment_id:
                assignment_obj=Assignment.objects.get(id=i)
               
                
                comment=Comment.objects.get(id=pk)
               
                comment.assignment.add(assignment_obj)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
       
        
       


   
 
    
   
        
       
