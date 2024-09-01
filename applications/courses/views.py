from django.shortcuts import render
from drf_yasg.openapi import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

from applications.buy_courses.models import BuyCourse
from applications.courses.models import Course
from applications.courses.serializers import CourseSerializer


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


