from rest_framework import permissions

# These are custom permission classes which inherits BasePermission class


#Only admin can create/update/delete and others can read_only

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        

#Only Reviewed user or Admin can make changes to the Review and other can read_only

class IsReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user==request.user or request.user.is_staff