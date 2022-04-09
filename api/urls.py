
from django.urls import path,include
from api import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("users",views.UserView,basename="users")
router.register("assignments",views.AssignmentView,basename="assignment")
urlpatterns = [
    
    path('',include(router.urls)),
]
