from django.shortcuts import render
from rest_framework import viewsets, status, filters 
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message, CustomUser
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated
from .filters import MessageFilter
from .pagination import MessagePagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all() # Ensure this queryset is filtered to only include conversations the user is a participant of
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()  # Ensure this queryset is filtered to only include messages in conversations the user is a participant of
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    pagination_class = MessagePagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

