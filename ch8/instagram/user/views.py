from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import CustomUser, Follow
from user.serializers import UserSignUpSerializer, UserMeResponseSerializer, UserMeUpdateSerializer, \
    UserFollowResponseSerializer


# Create your views here.
class UserSignUpView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSignUpSerializer
    # CreateAPIView를 상속받아 POST 요청을 처리하여 사용자 생성

class UserMeView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserMeResponseSerializer
    permission_classes = [IsAuthenticated] # 인증된 사용자만 접근 허용
    authentication_classes = [JWTAuthentication] # JWT 인증 사용

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserMeResponseSerializer
        elif self.request.method in ["PUT", "PATCH"]:
            return UserMeUpdateSerializer
        return super().get_serializer_class()

class UserFollowView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, user_id):
        if user_id == request.user.id:
            raise PermissionDenied("자기 자신을 팔로우 할 수 없습니다.")

        # 조회 또는 생성
        # 조회 -> 결과 반환
        # 조회 X -> 생성 후 결과 반환
        follow, created = Follow.objects.get_or_create(
            user_id=user_id, follower_id=request.user.id
        )
        serializer = UserFollowResponseSerializer(follow)

        if created:
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.data, status=status.HTTP_200_OK)