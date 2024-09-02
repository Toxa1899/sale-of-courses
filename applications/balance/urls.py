from rest_framework import routers
from django.urls import path, include
from applications.balance.views import BalanceViewSet, BalancePaidAPIView

router = routers.DefaultRouter()
router.register(r'balance', BalanceViewSet)
# router.register(r'balance/paid', BalancePaidAPIView)


urlpatterns = [
    path('', include(router.urls)),
    path('balance/paid/<uuid:uuid>/', BalancePaidAPIView.as_view())

]