from django.urls import path
from post import views

urlpatterns = [
    path("", views.posts_view, name="posts"), # 전체게시글 목록
    path("<int:post_id>/", views.post_view, name="post"), #  상세 게시글 조회
    path("<int:post_id>/like/", views.post_like_view, name="post_like"), # 게시글 좋아요
]