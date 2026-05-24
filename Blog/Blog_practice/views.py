from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from Blog_practice.models import Blog, Comment
from Blog_practice.serializers import (
    BlogListSerializer, BlogDetailSerializer,
    BlogCreateUpdateSerializer, CommentSerializer
)


class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data)

    def patch(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = BlogCreateUpdateSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentListView(APIView):
    def get(self, request, pk):
        comments = Comment.objects.filter(blog_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
