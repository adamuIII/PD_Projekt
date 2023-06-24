from .models import Developer, Category, Game
from rest_framework import serializers

# Serializery powoduja, ze obiekt z bazy danych zamieniany jest na obiekt JSON
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ["developer", "slug"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category", "slug"]

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["category", "developer", "title", "description", "instock", "price", "release_date", "creation_date", "slug"]