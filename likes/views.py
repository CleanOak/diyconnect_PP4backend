from rest_framework import generics, permissions
from diy_connect.permissions import IsOwnerReadOnly
from .models import Like
from .serializers import LikeSerializer

from notifications.models import Notification


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        like = serializer.save(owner=self.request.user)

        # Create a notification for the post owner (if not liking their own post)
        if like.post.owner != self.request.user:
            Notification.objects.create(
                user=like.post.owner,  # The recipient of the notification
                sender=self.request.user,  # The user who liked the post
                post=like.post,  # The post that was liked
                type="like",  # Notification type
            )


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



