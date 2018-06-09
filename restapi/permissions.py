from rest_framework.permissions import BasePermission
from citizens.models import Profile


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsUser(BasePermission):
    def has_permission(self, request, view):
        if "user" in request.data:
            return request.data["user"] == request.user.id
        else:
            return request.data["user_id"] == request.user.id


class IsInDebate(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.phase.slug == "debate"


class IsInReview(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.phase.slug == "review"
