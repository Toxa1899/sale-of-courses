from rest_framework import viewsets, permissions
from .models import ProductCard, ProductCardImage
from .serializers import ProductCardSerializer, ProductCardImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, action
from rest_framework.authentication import SessionAuthentication

from ..courses.models import Course
from ..courses.serializers import CourseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductCard.objects.all()
    serializer_class = ProductCardSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        courses = Course.objects.filter(product_card=instance)
        course_serializer = CourseSerializer(courses, many=True)
        data['Course'] = course_serializer.data

        return Response(data)


class ProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductCardImage.objects.all()
    serializer_class = ProductCardImageSerializer


