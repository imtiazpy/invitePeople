from django.contrib.auth import get_user_model
from rest_framework import serializers

from djoser.serializers import UserCreateSerializer



User = get_user_model()


class UserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password', )




class UserActivationSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()