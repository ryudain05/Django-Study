from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

# 1:1
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

# user1 - profile1(on_delete=CASCADE)
# xxx - profile1(on_delete=CASCADE)

# 1:M
class Order(models.Model):
    price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

# N:M
class Project(models.Model):
    name = models.CharField(max_length=20)
#     users = models.ManyToManyField(CustomUser, through="ProjectUser")
#
# class ProjectUser(models.Model):
#     customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'orm_project_user'

class UserProjectRelation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)