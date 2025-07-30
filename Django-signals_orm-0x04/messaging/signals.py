from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Message, Notification, MessageHistory

User = get_user_model()

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.id:
        try:
            old_instance = Message.objects.get(pk=instance.id)
            if old_instance.content != instance.content:
                # Save old content
                MessageHistory.objects.create(
                    message=old_instance,
                    old_content=old_instance.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass        


@receiver(post_delete, sender=User)
def clean_user_data(sender, instance, **kwargs):
    # Messages where user was sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Notifications
    Notification.objects.filter(user=instance).delete()

    # Message histories related to user's messages
    MessageHistory.objects.filter(message__sender=instance).delete()
