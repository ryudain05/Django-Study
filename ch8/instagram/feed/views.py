from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import CursorPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response

from feed.models import Post, PostComment
from feed.serializers import PostSerializer, PostCommentCreateSerializer


class PostCursorPagination(CursorPagination):
    page_size = 1
    ordering = '-created_at'

# Create your views here.
class PostView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = PostCursorPagination # 특정 API 뷰에서 커서 페이지네이션을 사용하도록 설정

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

class PostCommentView(CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        request.data["post_id"] = self.kwargs.get("post_id")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)