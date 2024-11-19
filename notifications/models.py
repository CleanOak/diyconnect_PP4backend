from django.contrib.auth.models import User
from django.db import models
from posts.models import Post

class Notification(models.Model):
    """
    Notification model relating to post, profile,
    comment, like
    """
    TYPE_CHOICES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name='notifications')  # Recipient
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    class Meta:
        """
        Class to order in descending order
        """
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for {self.owner}"
