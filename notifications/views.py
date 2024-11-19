from rest_framework import generics, permissions
from diy_connect.permissions import IsOwnerReadOnly
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListCreateAPIView):
    """
    List all notifications for the logged-in user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Notification.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
class NotificationDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve, update, or delete a specific notification.
    Mark notification as read using PATCH or update.
    """
    permission_classes = [IsOwnerReadOnly]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
