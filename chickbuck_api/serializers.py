from rest_framework import serializers
from .models import Category,Items


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = '__all__'