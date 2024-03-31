from rest_framework import serializers
from .models import Drink, Snack



class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description', 'type']

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ['id', 'name', 'description', 'type']