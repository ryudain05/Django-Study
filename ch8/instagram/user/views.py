from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from user.models import CustomUser
from user.serializers import UserSignUpSerializer

# Create your views here.
class UserSignUpView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSignUpSerializer
    # CreateAPIView를 상속받아 POST 요청을 처리하여 사용자 생성