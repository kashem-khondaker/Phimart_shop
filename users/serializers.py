from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id' , 'email' , 'password' , 'first_name' , 'last_name' , 'address' , 'phone']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer):
        model = get_user_model()
        fields = ['id' , 'email' , 'first_name' , 'last_name' , 'address' , 'phone']

