from rest_framework import generics, permissions
from django.db.models import Count
from .models import Bookmark
from .serializers import BookmarkSerializer

class BookmarkList(generics.ListAPIView):
    """
    List all bookmarks for the logged-in user.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return bookmarks for the logged-in user.
        """
        return Bookmark.objects.filter(user=self.request.user).annotate(
            post_likes_count=Count('post__likes', distinct=True)
        ).order_by('-created_at')


class BookmarkDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific bookmark.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only access their own bookmarks.
        """
        return Bookmark.objects.filter(user=self.request.user)

