from rest_framework import generics, permissions
from diy_connect.permissions import IsOwnerReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer

class BookmarkList(generics.ListCreateAPIView):
    """
    List all bookmarks for the logged-in user.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve, update, or delete a specific bookmark.
    """
    permission_classes = [IsOwnerReadOnly]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer