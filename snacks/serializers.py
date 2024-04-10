from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Drink, Snack


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description', 'type']


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ['id', 'name', 'description', 'type']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username already exists')

        return data

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        #print(dir(user))
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

