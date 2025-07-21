# chats/permissions.py

from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to:
    - Allow only authenticated users globally
    - Allow only participants of a conversation to view, send, update, or delete messages
    """

    def has_object_permission(self, request, view, obj):
        # For Conversation object
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()

        # For Message object (assumes obj has .conversation)
        if hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()

        return False

# class IsParticipant(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user in obj.participants.all()

# class IsMessageParticipant(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return (
#             obj.sender == request.user or
#             request.user in obj.conversation.participants.all()
#         )
