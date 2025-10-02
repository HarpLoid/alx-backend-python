from django.db import models
from uuid import uuid4
from chats.models import User

class UnreadMessageManager(models.Manager):
    def for_user(self, user):
        """
        Return only unread messages for a specific user.
        Optimized to fetch only required fields.
        """
        return (
            self.get_queryset()
            .filter(receiver=user, read=False)
            .only('id', 'sender', 'content', 'sent_at')
            .select_related('sender')
        )

class Message(models.Model):
    """
    Message model
    """
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField()
    parent_message = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    read = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    unread = UnreadMessageManager()
    objects = models.Manager()
    
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"

class MessageHistory(models.Model):
    """
    Message history model
    """
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE,
        related_name='edit_history'
    )
    old_message = models.TextField()
    edited_at  = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    """
    Stores notifications linking it to the User and Message models
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='notifications'
    )
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE,
        related_name='notifications'
    )
    create_at = models.DateTimeField(auto_now_add=True)
