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