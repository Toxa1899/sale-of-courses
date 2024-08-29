from rest_framework import viewsets, permissions
from .models import ProductCard, ProductCardImage
from .serializers import ProductCardSerializer, ProductCardImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductCard.objects.all()
    serializer_class = ProductCardSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductCardImage.objects.all()
    serializer_class = ProductCardImageSerializer


