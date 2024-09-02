from django.shortcuts import render
from drf_yasg.openapi import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

from applications.buy_courses.models import BuyCourse
from applications.courses.models import Course
from applications.courses.serializers import CourseSerializer
from rest_framework.exceptions import PermissionDenied

# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

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
