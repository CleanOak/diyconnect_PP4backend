from rest_framework import generics, permissions
from diy_connect.permissions import IsOwnerReadOnly
from .models import Follower
from .serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user'.
    Create a follower, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        follow = serializer.save(owner=self.request.user)

         # Create a notification for the post owner (if not follow on their profile)
        if follow.post.owner != self.request.user:
            Notification.objects.create(
                user=follow.post.owner,  # The recipient of the notification
                sender=self.request.user,  # The user who commented
                post=follow.post,  # The post that was commented on
                type="follow",  # Notification type
            )


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    No Update view, as we either follow or unfollow users
    Destroy a follower, i.e. unfollow someone if owner
    """
    permission_classes = [IsOwnerReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
