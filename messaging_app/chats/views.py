from .models import User
from .filters import MessageFilter
from django.shortcuts import render
from .serializers import UserSerializer
from .models import Message, Conversation
from .pagination import MessagePagination
from rest_framework.response import Response
from rest_framework import viewsets, filters
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MessageSerializer, ConversationSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ConversationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]
    
    def perform_create(self, serializer):
        serializer.save(participants_id=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and creating messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = MessageFilter
    search_fields = ['message_body']
    pagination_class = MessagePagination
    permission_classes = [IsParticipantOfConversation]
    
    def get_queryset(self):
        # Retrieve the conversation_id from the URL and filter messages
        conversation_id = self.kwargs.get('conversation_id')
        return Message.objects.filter(conversation_id=conversation_id)

    def perform_create(self, serializer):
        # The conversation object is available via a nested router's lookup
        conversation = Conversation.objects.get(
            id=self.kwargs.get('conversation_id')
        )
        serializer.save(sender_id=self.request.user, conversation=conversation)
    
