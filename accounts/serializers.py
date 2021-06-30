from rest_framework import serializers
from .models import UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if(validated_data.get('password')!=None):
            instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance

class UserSerializerWithTokens(UserSerializer):
    refresh = serializers.SerializerMethodField(read_only = True)
    access = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = UserAccount
        fields = ['id', 'first_name', 'last_name', 'email', 'refresh', 'access']

    def get_refresh(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)
    
    def get_access(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class CustomTokenObtainPairViewSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializer(self.user).data
        for key, value in serializer.items():
            data[key] = value
        return data