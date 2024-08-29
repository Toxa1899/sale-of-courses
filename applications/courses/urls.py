from rest_framework import routers
from django.urls import path, include

from applications.courses.views import CourseViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]
