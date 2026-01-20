from django.db import models

from user.models import CustomUser


# Create your models here.

# images/
# a.png
# b.png
class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to="images")