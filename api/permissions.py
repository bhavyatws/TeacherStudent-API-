from rest_framework import permissions


class TeacherOnly(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH","POST","DELETE")
    def has_object_permission(self, request, view, obj):
            if request.user.is_teacher:
                return True

            return False

class OwnerOnly(permissions.BasePermission):
     def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj here is a UserProfile instance
        return obj.user == request.user