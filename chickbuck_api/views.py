from django.shortcuts import render
from .models import Category,Items
from rest_framework.response import Response 
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import CategorySerializer,ItemsSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.decorators import action




class CategoryView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def list(self, request, *args, **kwargs):
    #     # Get all categories
    #     queryset = self.get_queryset()
        
    #     # Serialize the categories
    #     serializer = self.get_serializer(queryset, many=True)

    #     # Return the serialized data as response
    #     return Response(serializer.data)
    


class ItemsView(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [IsAuthenticated]