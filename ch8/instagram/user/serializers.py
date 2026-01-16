from rest_framework import serializers
from user.models import CustomUser

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"] # id 필드는 읽기 전용, 생성 시에만 사용

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user


# serializers.save() 호출 시 비밀번호를 해싱하여 저장
# CustomUser.oejbcts.create_user() 메서드를 사용하여 비밀번호를 안전하게 저장 / 일반 create() 메서드는 비밀번호를 해싱하지 않음