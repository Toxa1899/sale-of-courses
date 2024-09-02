from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.buy_courses.models import BuyCourse
from applications.buy_courses.serializers import BuyCourseSerializer, BuyCoursePostSerializer, BuyCoursesInfoSerializer


# Create your views here.


class BuyCoursesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BuyCoursePostSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        course = BuyCourse.objects.filter(user=request.user)
        serializers = BuyCourseSerializer(course, many=True)
        return Response(serializers.data)



class BuyCoursesInfoAPIView(APIView):
    def get(self, request):
        courses = BuyCourse.objects.filter(product_card__user=request.user)
        serializer = BuyCoursesInfoSerializer(courses, many=True)
        return Response(serializer.data)
