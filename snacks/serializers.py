from django.contrib.auth import authenticate
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


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    # def validate(self, data):
    #     try:
    #         user = authenticate(username=data['username'], password=data['password'])
    #         if not user:
    #             raise serializers.ValidationError("Username or password is incorrect")
    #
    #     return data

    def create(self, validated_data):

        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError('username already exists')

        user = User.objects.create(username=validated_data['username'])
        #print(dir(user))
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

    def delete(self, validated_data):
        u = authenticate(username=validated_data['username'], password=validated_data['password'])
        if not u:
            raise serializers.ValidationError('Invalid credentials')
        user = User.objects.get(username=validated_data['username'])
        user.delete()
        return validated_data



