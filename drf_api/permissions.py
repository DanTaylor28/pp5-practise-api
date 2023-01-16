from rest_framework import permissions


class IsPostOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


# Custom permission to only allow the admin to create,
# update and delete but everyone else can read (for categories primarily)
class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super(
            IsAdminOrReadOnly,
            self).has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin
