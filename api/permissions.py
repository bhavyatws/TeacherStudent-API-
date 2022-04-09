from rest_framework import permissions


class TeacherOnly(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH","POST")
    def has_object_permission(self, request, view, obj):
            if request.user.is_teacher:
                return True

            return False