from enum import auto
from operator import mod
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from django.utils.timezone import now
from .manager import CustomUserManager

# Create your models here.

#Create your customuser model here


#Create your user model here

class User(AbstractBaseUser,PermissionsMixin):
    #AbstractBaseUser has password,last_login,is_active by default
    username=models.CharField(db_index=True,max_length=50,unique=True)
    email=models.EmailField(db_index=True,unique=True,max_length=254,null=True,blank=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    date_joined=models.DateTimeField(default=now)
    is_teacher=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)#must need,otherwise you will not able to login
    is_active=models.BooleanField(default=True)#must need,otherwise you will not able to login
    is_superuser=models.BooleanField(default=False)#This is inherited Permissions
    objects=CustomUserManager()
    # EMAIL_FIELD='email'
    USERNAME_FIELD='username'
    REQUIRED_FIELD = []
    class Meta:
        verbose_name='user'
        verbose_name_plural='users'
    def __str__(self):
        return self.username
   
from django.contrib.auth import get_user_model
User = get_user_model()


class Assignment(models.Model):
    
    name=models.CharField(max_length=100,null="",blank=True)
    description=models.CharField(max_length=250,null="",blank=True)
    timestamp=models.DateTimeField(auto_now=True)
    teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='teacher')
    student=models.ManyToManyField(User)
   
    # comment=models.ManyToManyField('Comment')

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #by giving related name,we can use this to which it has relation
    assignment=models.ManyToManyField(Assignment,related_name="comment")
    comment=models.TextField()
    timestamp=models.DateTimeField(auto_now=True)