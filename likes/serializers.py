from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


# class LikeSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')


#     class Meta:
#         model = Like
#         fields = [
#             'id', 'owner', 'post', 'created_at'
#         ]
    
#     def create(self, validated_data):
#         try:
#             return super().create(validated_data)
#         except IntegrityError:
#             raise serializers.ValidationError({
#                 'detail': 'possible duplicate'
#             })

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'owner', 'post', 'created_at']

    def create(self, validated_data):
        try:
            # Create the like instance
            like = super().create(validated_data)
            
            # Check if the post owner is not the same as the liking user
            if like.post.owner != like.owner:
                # Create a notification for the post owner (if not liking their own post)
                Notification.objects.create(
                    user=like.post.owner,  # The recipient of the notification (post owner)
                    sender=like.owner,  # The user who liked the post
                    post=like.post,  # The post that was liked
                    type="like",  # Notification type
                )

            return like

        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible duplicate like'
            })