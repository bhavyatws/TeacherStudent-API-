
from django.urls import path,include
from api import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("users",views.UserView,basename="users")
router.register("assignments",views.AssignmentView,basename="assignment")
router.register("comment",views.CommentView,basename="comment")
urlpatterns = [
    
    path('',include(router.urls)),
    
    # path('add-remove-student/',views.reverse_action('set-password', args=['1']))
]
