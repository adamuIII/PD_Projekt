from .models import Developer, Category, Game
from rest_framework import serializers

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ["developer"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["category", "developer", "title", "description", "instock", "price", "release_date", "creation_date"]