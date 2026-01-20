from django.urls import path

from feed import views

urlpatterns = [
    path("posts/", views.PostView.as_view(), name="posts"),
]