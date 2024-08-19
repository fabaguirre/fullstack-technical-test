from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsVolunteer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "volunteer"


class IsAdopter(permissions.BasePermission):
    def has_permission(self, request, view):
        # print all the attributes of request.user
        print(dir(request))
        return request.user.is_authenticated and request.user.role == "adopter"
