from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Blog_practice.serializers import BlogListSerializer, BlogDetailSerializer
from Blog_practice.models import Blog

# Create your views here.

# 블로그 목록에 대해서 실행
# - GET: 목록 조회
# - POST: 목록에 새 블로그 추가
@api_view(["GET", "POST"])
def blog_list(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True)

        return Response(serializer.data) # status=200
    else:
        serializer = BlogDetailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 단일 블로그에 대해 실행
# - GET: 블로그 조회
# - PATCH: 블로그 내용 수정
# - DELETE: 블로그 삭제
@api_view(["GET", "PATCH", "DELETE"])
def blog_detail(request, pk):
    if request.method == "GET":
        blog = get_object_or_404(Blog, id=pk)
        serializer = BlogDetailSerializer(blog)

        return Response(serializer.data) # status=200
    elif request.method == "PATCH":
        blog = get_object_or_404(Blog, id=pk)
        # partial=True: 시리얼라이저의 일부 필드만 채워져도 OK
        serializer = BlogDetailSerializer(blog, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data) # status=200
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # 삭제는 Serializer의 관심사가 아니므로 Serializer를 쓰지 않습니다!
        blog = get_object_or_404(Blog, id=pk)
        blog.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
