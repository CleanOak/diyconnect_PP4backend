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

       
class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



