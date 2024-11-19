from rest_framework import generics, permissions
from diy_connect.permissions import IsOwnerReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        comment = serializer.save(owner=self.request.user)

        # Create a notification for the post owner (if not commenting on their own post)
        if comment.post.owner != self.request.user:
            Notification.objects.create(
                user=comment.post.owner,  # The recipient of the notification
                sender=self.request.user,  # The user who commented
                post=comment.post,  # The post that was commented on
                type="comment",  # Notification type
            )


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
