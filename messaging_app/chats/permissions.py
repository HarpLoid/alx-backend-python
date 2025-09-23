from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    Assumes the view has a `get_conversation` method that returns the conversation instance.
    """
    def has_object_permission(self, request, view, obj):
        conversation = view.get_conversation()
        return conversation and request.user in conversation.participants_id.all()