from django.urls import path
from post import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="posts"), # 전체게시글 목록
    path("create/", views.PostCreateView.as_view(), name="post_create"), #  게시글 작성
    path("<int:post_id>/", views.PostDetailView.as_view(), name="post"), #  상세 게시글 조회
    path("<int:post_id>/like/", views.PostLikeView.as_view(), name="post_like"), # 게시글 좋아요
]