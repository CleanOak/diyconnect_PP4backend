from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Bookmark(models.Model):
    """
    Bookmark model relating to post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="bookmarked_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class to order in descending order
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f"{self.owner} bookmarked {self.post}"
