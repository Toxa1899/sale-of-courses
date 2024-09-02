from django.urls import path
from applications.buy_courses.views import BuyCoursesAPIView, BuyCoursesInfoAPIView

urlpatterns = [
    path('', BuyCoursesAPIView.as_view(), name='buy_courses'),
    path('info/', BuyCoursesInfoAPIView.as_view(), name='buy_courses_info')
]

