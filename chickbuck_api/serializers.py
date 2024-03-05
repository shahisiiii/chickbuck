from rest_framework import serializers
from .models import Category,Items,CartItem


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ItemsSerializer(serializers.ModelSerializer):

    category_name = serializers.ReadOnlyField(source='category.category')

    class Meta:
        model = Items
        fields = ['id', 'name', 'description', 'price', 'is_favourite', 'category_name', 'item_image']


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'