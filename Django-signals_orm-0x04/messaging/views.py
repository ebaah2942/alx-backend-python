from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from messaging.models import Message

# Create your views here.

User = get_user_model()

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)  # Log out before deleting
        user.delete()
        return redirect('account_deleted')  # Replace with your URL or success message
    return HttpResponseForbidden("You can't access this directly.")


@login_required
def conversation_view(request):
    # Fetch top-level messages where user is either sender or receiver
    messages = Message.objects.filter(
        parent_message__isnull=True
    ).filter(
        sender=request.user
    ) | Message.objects.filter(
        parent_message__isnull=True,
        receiver=request.user
    )

    # Optimize query
    messages = messages.select_related('sender', 'receiver').prefetch_related('replies__sender', 'replies__receiver')

    return render(request, 'messaging/conversation.html', {'messages': messages})


@login_required
def unread_messages_view(request):
    unread_messages = Message.unread.unread_for_user(request.user).only('id', 'sender', 'content', 'timestamp')
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_messages})

