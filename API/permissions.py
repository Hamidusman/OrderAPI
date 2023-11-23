from rest_framework import permissions

class CustomerOrReadOnly(permissions.BasePermission):
    def object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.customer == request.user