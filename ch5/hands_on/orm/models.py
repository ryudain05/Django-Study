import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    # media/profiles/image.png
    image = models.ImageField(upload_to='profiles/', null=True)


