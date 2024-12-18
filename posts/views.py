from rest_framework import generics, permissions, filters
from diy_connect.permissions import IsOwnerReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from django.db.models import Count
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count =Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        bookmark_count=Count('bookmarks', distinct=True)
    ).order_by('created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'bookmarks__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comment_count',
        'bookmark_count',
        'likes_created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        bookmark_count=Count('bookmarks', distinct=True)
    ).order_by('-created_at')