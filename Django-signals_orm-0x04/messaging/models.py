from django.db import models
from uuid import uuid4
from chats.models import User

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
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"

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
