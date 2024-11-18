from django.urls import path
from notifications import views

urlpatterns = [
    path('notifications/', views.NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:id>/', views.NotificationDetail.as_view(), name='notification-detail'),
]