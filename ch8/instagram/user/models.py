from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email' # 기본 인증에 사용하는 필드를 변경
    REQUIRED_FIELDS = ['username'] # 추가적인 필수 입력받을 필드 지정

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

class Follow(models.Model):
    user = models.ForeignKey(CustomUser, related_name="followers", on_delete=models.CASCADE) # 나를 팔로우하고 있는 사용자들 집합
    follower = models.ForeignKey(CustomUser, related_name="followings", on_delete=models.CASCADE) # 내가 팔로우하고 있는 사용자들 집합
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'follower'], name='unique_follow_relationship')
        ]
        ordering = ['-created_at'] # 최신 팔로우가 먼저 오도록 정렬

    def __str__(self):
        return f"{self.follower_id} -> {self.user_id}"