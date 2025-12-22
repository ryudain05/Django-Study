import string
import random
from email.policy import default

from django.db import models

# Create your models here.
class ShortURL(models.Model):
    # bit.ly/x => google.com, 중복 방지를 위한 unique
    code = models.CharField(max_length=8, unique=True)
    original_url = models.URLField(max_length=200)
    access_count = models.PositiveIntegerField(default=0) # 양의 정수 컬럼
    created_at = models.DateTimeField(auto_now_add=True)

    # {app_label}_{클래스 이름 소문자}
    # db table: shortener_shorturl -> short_url
    class Meta:
        app_label = 'shortener'
        db_table = 'short_url'


    @staticmethod
    def generate_code():
        characters = string.ascii_letters + string.digits
        return "".join(random.choices(characters, k=8))