from rest_framework import serializers
from accounts.serializers import CustomUserSerializer

class BlogSerializer(serializers.Serializer):
    user = CustomUserSerializer(serializers.Serializer)
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(default="")
    date = serializers.DateTimeField(read_only=True)

    def get_user(self, obj):
        return obj.user.username