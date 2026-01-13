from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from shortener.models import ShortURL
from shortener.serializers import ShortURLResponseSerializer, ShortURLCreateSerializer


class ShortURLAPIView(APIView):
    def get(self, request):
        short_urls = ShortURL.objects.all()
        serializer = ShortURLResponseSerializer(short_urls, many=True)
        return Response(data=serializer.data) # JSON 데이터

    def post(self, request):
        serializer = ShortURLCreateSerializer(data=request.data) # drf는 request.data 사용(기존: request.POST)
        if serializer.is_valid():
            while True:
                code = ShortURL.generate_code()
                if not ShortURL.objects.filter(code=code).exists():
                    break

            short_url = serializer.save(code=code)
            return Response(
                data=ShortURLResponseSerializer(short_url).data,
                status=201,
            )

class ShortURLDetailAPIView(APIView):
    def delete(self, request, code):
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.delete()
        return Response(status=204)
