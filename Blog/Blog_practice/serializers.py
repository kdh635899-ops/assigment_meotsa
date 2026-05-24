from rest_framework import serializers
from Blog_practice.models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source='date', read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "blog_id", "comment", "created_at"]
        read_only_fields = ["id", "blog_id", "created_at"]


class BlogListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source='date', read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at"]


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(source='date', read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at", "comments"]
        read_only_fields = ["id", "created_at", "comments"]


class BlogCreateUpdateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source='date', read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at"]
        read_only_fields = ["id", "created_at"]