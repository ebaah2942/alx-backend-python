# chats/permissions.py

from rest_framework import permissions

class IsParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()

class IsMessageParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.sender == request.user or
            request.user in obj.conversation.participants.all()
        )
