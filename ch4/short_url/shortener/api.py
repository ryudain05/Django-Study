from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import get_object_or_404, GenericAPIView, ListAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from shortener.models import ShortURL
from shortener.serializers import ShortURLResponseSerializer, ShortURLCreateSerializer


class ShortURLAPIView(ListCreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLResponseSerializer

    def perform_create(self, serializer):
        while True:
            code = ShortURL.generate_code()
            if not ShortURL.objects.filter(code=code).exists():
                break
        serializer.save(code=code)

    def create(self, request, *args, **kwargs):
        serializer = ShortURLCreateSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(data=ShortURLResponseSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShortURLDetailAPIView(DestroyAPIView):
    queryset = ShortURL.objects.all()
    lookup_field = "code"

class ShortURLViewSet(
    ListModelMixin, CreateModelMixin, DestroyAPIView,GenericViewSet
):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLResponseSerializer
    lookup_field = "code"

    def perform_create(self, serializer):
        while True:
            code = ShortURL.generate_code()
            if not ShortURL.objects.filter(code=code).exists():
                break
        serializer.save(code=code)

    def create(self, request, *args, **kwargs):
        serializer = ShortURLCreateSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(data=ShortURLResponseSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
