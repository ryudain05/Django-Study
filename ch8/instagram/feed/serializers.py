from rest_framework import serializers

from feed.models import Post


class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'image', 'description', 'created_at']
