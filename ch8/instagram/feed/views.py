from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import CursorPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from feed.models import Post
from feed.serializers import PostSerializer

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

