from django.urls import path

from user import views

urlpatterns = [
    path("", views.UserSignUpView.as_view(), name="user_sign_up"),
]