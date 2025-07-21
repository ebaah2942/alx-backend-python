# chats/permissions.py

from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to:
    - Allow only authenticated users globally
    - Allow only participants of a conversation to view, send, update, or delete messages
    """


    def has_permission(self, request, view):
        # ✅ Explicitly check for authentication
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        # Check participant for conversation or message
        if hasattr(obj, 'participants'):
            is_participant = request.user in obj.participants.all()
        elif hasattr(obj, 'conversation'):
            is_participant = request.user in obj.conversation.participants.all()
        else:
            return False

        # ✅ Check methods like PUT, PATCH, DELETE
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return is_participant  # Allow only participants to modify/delete

        # ✅ For GET or POST
        return is_participant

