from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import CustomUser
from user.serializers import UserSignUpSerializer, UserMeResponseSerializer


# Create your views here.
class UserSignUpView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSignUpSerializer
    # CreateAPIView를 상속받아 POST 요청을 처리하여 사용자 생성

class UserMeView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserMeResponseSerializer
    permission_classes = [IsAuthenticated] # 인증된 사용자만 접근 허용
    authentication_classes = [JWTAuthentication] # JWT 인증 사용

    def get_object(self):
        return self.request.user