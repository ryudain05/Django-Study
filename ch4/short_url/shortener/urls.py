from django.urls import path
from shortener import views, api

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("short-urls/", views.ShortURLCreateView.as_view(), name="shorten_url"),
    path("<str:code>/", views.ShortURLDetailView.as_view(), name="short_url_detail"),

    # drf
    path("api/short-urls/", api.ShortURLAPIView.as_view(), name="short_urls_api"),
]