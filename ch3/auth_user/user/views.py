import uuid

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from user.forms import CustomUserCreationForm
from django.conf import settings
import requests
import uuid
from django.contrib.auth.models import User
from django.http import JsonResponse

class HomeView(View):
    def get(self, request):
        # context = {"user": user, "perms": perms}
        return render(request, 'home.html')

class SignUpView(View):
    def get(self, request):
        return render(request, 'registration/sign_up.html', {"form": CustomUserCreationForm()})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user) # session login
        return redirect("home")

class KakoSocialLoginView(View):
    def get(self, request):
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize"
            f"?client_id={settings.KAKAO_REST_API_KEY}"
            f"&redirect_uri={settings.KAKAO_CALLBACK_URL}"
            f"&response_type=code"
        )

class KakoSocialCallbackView(View):
    def get(self, request):
        # http://127.0.0.1:8000/users/social/kakao/callback/?code=AUTH_CODE
        # kakao -> django
        auth_code = request.GET.get("code")

        # access token 교환
        response = requests.post(
            "https://kauth.kakao.com/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": settings.KAKAO_REST_API_KEY,
                "redirect_uri": settings.KAKAO_CALLBACK_URL,
                "code": auth_code,
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
            }
        )

        if response.ok:
            access_token = response.json().get("access_token")

            # 사용자의 카카오 프로필 조회
            profile_response = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers={"Authorization": f"Bearer {access_token}"}
            )

            if profile_response.ok:
                # 사용자 프로필 정보 => 회원가입/로그인 처리
                username = f"K#{profile_response.json()['id']}"  # 임의로 username 생성
                # K#123

                try:
                    #기존 회원 여부
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    #신규 회원 가입
                    email = profile_response.json()["kakao_account"]["email"]
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=str(uuid.uuid4()),
                        social_provider="kakao"
                    )

                login(request, user)
                return redirect("home")

        return JsonResponse({'error': '카카오 로그인 실패'}, status=400)re