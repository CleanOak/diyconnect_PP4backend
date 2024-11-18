from django.contrib.auth.models import User
from django.db import models
from posts.models import Post
from profiles.models import Profile
from comments.models import Comment
from likes.models import Like


class Notification(models.Model):
    """
    Notification model relating to post, profile,
    comment, like
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="notifications")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
    null=True, blank=True, related_name="notifications")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
    null=True, blank=True, related_name="notifications")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
    null=True, blank=True, related_name="notifications")
    like = models.ForeignKey(Like, on_delete=models.CASCADE, null=True,
    blank=True, related_name="notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models. DateTimeField(auto_now_add=True)


    class Meta:
        """
        Class to order in descending order
        """
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for {self.owner}"