from rest_framework import generics, permissions
from django.db.models import Count
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    """
    List all notifications for the logged-in user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return notifications for the logged-in user.
        """
        return Notification.objects.filter(user=self.request.user).annotate(
            likes_count=Count('like', distinct=True)
        ).order_by('-created_at')


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific notification.
    Mark notification as read using PATCH or update.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only access their own notifications.
        """
        return Notification.objects.filter(user=self.request.user)
