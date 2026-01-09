from rest_framework import serializers
from shortener.models import ShortURL


# 1) 클라이언트 요청 -> serializer -> 서버 -> 역직렬화, Deserialize
# 2) 서버 응답 -> serializer -> 클라이언트 -> 직렬화 , Serialize
class ExampleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class ShortURLResponseSerializer(serializers. ModelSerailzer):
    class Meta:
        model = ShortURL
        fields = "__all__"