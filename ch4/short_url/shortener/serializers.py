from rest_framework import serializers
from shortener.models import ShortURL


# 1) 클라이언트 요청 -> serializer -> 서버 -> 역직렬화, Deserialize
# 2) 서버 응답 -> serializer -> 클라이언트 -> 직렬화 , Serialize
class ExampleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class ShortURLResponseSerializer(serializers. ModelSerializer):
    class Meta:
        model = ShortURL
        fields = "__all__"

class ShortURLCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ["original_url"]  # 클라이언트가 제공해야 하는 필드