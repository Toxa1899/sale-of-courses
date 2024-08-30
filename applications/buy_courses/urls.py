from django.urls import path
from applications.buy_courses.views import BuyCoursesAPIView

urlpatterns = [
    path('', BuyCoursesAPIView.as_view(), name='buy_courses')
]

