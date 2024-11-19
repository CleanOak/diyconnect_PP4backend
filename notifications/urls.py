from django.urls import path
from .views import NotificationList, NotificationDetail, UnreadNotificationCount

urlpatterns = [
    path('notifications/', NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:id>/', NotificationDetail.as_view(), name='notification-detail'),
    path('notifications/unread-count/', UnreadNotificationCount.as_view(), name='unread-count'),
]
