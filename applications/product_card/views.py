from rest_framework import viewsets, permissions
from .models import ProductCard, ProductCardImage
from .serializers import ProductCardSerializer, ProductCardImageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, action
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import PermissionDenied
from ..buy_courses.models import BuyCourse
from ..courses.models import Course
from ..courses.serializers import CourseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductCard.objects.all()
    serializer_class = ProductCardSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        courses = Course.objects.filter(product_card=instance)
        if (not BuyCourse.objects.filter(user=user, product_card=instance).exists()
                and not Course.objects.filter(user=user)):
            data['Course'] = "Вы не приобрели данный курс"
        else:
            course_serializer = CourseSerializer(courses, many=True)
            data['Course'] = course_serializer.data

        return Response(data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied('You do not have permission to update this course.')
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied('You do not have permission to delete this course.')

        self.perform_destroy(instance)
        return Response(status=204)


class ProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ProductCardImage.objects.all()
    serializer_class = ProductCardImageSerializer


