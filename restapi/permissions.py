from rest_framework.permissions import BasePermission
from citizens.models import Profile

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
