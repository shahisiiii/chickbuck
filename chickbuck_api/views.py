from django.shortcuts import render
from .models import Category,Items,CartItem
from rest_framework.response import Response 
from rest_framework import viewsets,status
from django.contrib.auth.models import User
from .serializers import CategorySerializer,ItemsSerializer,CartItemSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.decorators import action




class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryReadOnlyView(viewsets.ReadOnlyModelViewSet):
    """
    This view created for only read data for users
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    


class ItemsView(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ItemsSerializer
    queryset = Items.objects.all()

class ItemReadOnlyView(viewsets.ReadOnlyModelViewSet):
    """
    This view created for only read Category data for users
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ItemsSerializer
    queryset = Items.objects.all()
    
class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        # Extract data from request
        user = request.user
        item_id = request.data.get('item_id')  # Assuming item_id is provided in request data
        print(item_id)
        quantity = int(request.data.get('quantity', 1))

        if not item_id:
            return Response({'detail': 'Item ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch item details
        try:
            item = Items.objects.get(pk=item_id)
        except Items.DoesNotExist:
            return Response({'detail': 'Invalid item ID.'}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate price
        price = item.price * quantity

        # Create cart item
        cart_item = CartItem.objects.create(
            user=user,
            items=item,
            quantity=quantity,
            price=price
        )

        # Serialize and return response
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)