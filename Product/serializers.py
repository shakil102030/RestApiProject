from rest_framework import serializers
from .models import Category, Food


class CategoryListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name','description', 'categoryThumb')


class FoodListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'title', 'description')