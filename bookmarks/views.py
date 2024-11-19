from rest_framework import generics, permissions
from diy_connect.permissions import IsOwnerReadOnly
from django.db.models import Count
from .models import Bookmark
from .serializers import BookmarkSerializer

class BookmarkList(generics.ListAPIView):
    """
    List all bookmarks for the logged-in user.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     """
    #     Return bookmarks for the logged-in user.
    #     """
    #     return Bookmark.objects.filter(user=self.request.user).annotate(
    #         post_likes_count=Count('post__likes', distinct=True)
    #     ).order_by('-created_at')


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve, update, or delete a specific bookmark.
    """
    permission_classes = [IsOwnerReadOnly]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer