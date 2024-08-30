from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.buy_courses.serializers import BuyCourseSerializer


# Create your views here.


class BuyCoursesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializers = BuyCourseSerializer(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response('успешно', status=201)
