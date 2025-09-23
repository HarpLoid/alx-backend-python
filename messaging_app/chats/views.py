from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter
from .models import Message, Conversation
from .permissions import IsParticipantOfConversation
from .pagination import MessagePagination
from .serializers import MessageSerializer, ConversationSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    from .models import User
    from .serializers import UserSerializer
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ConversationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and creating conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    
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
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    
    def perform_create(self, serializer):
        serializer.save(sender_id=self.request.user)
    
    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation_id')
        try:
            conversation = Conversation.objects.get(conversation_id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({'error': 'Conversation not found.'}, status=404)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    
