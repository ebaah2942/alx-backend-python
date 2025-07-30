# messaging/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('delete_account/', delete_user, name='delete_user'),
    path('conversation/', conversation_view, name='conversation_view'),
    path('unread_messages/', unread_messages_view, name='unread_messages_view'),
]
