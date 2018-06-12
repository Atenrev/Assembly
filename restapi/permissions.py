from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return int(request.data["user"]) == request.user.id


class IsInDebate(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.phase.slug == "debate"


class IsInReview(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.phase.slug == "review"
