from shortener import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("short-urls/", views.ShortURLCreateView.as_view(), name="shorten_url"),
    path("<str:code>/", views.ShortURLDetailView.as_view(), name="short_url_detail"),

    # drf
    # path("api/", views.HomeView.as_view(), name="home_api"),
    # path("api/short-urls/", views.ShortURLCreateView.as_view(), name="shorten_url_api"),
    # path("api/<str:code>/", views.ShortURLDetailView.as_view(), name="short_url_detail_api"),
]