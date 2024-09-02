from decimal import Decimal

from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.models import CustomUser
from applications.balance.models import Balance
from applications.balance.serializers import BalanceSerializer, BalancePaidSerializer





class BalanceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class BalancePaidAPIView(APIView):
    def get(self, request, uuid):
        balance_q = Balance.objects.filter(link_uuid=uuid).first()
        if not balance_q:
            return Response({'error': 'Balance not found.'}, status=404)
        serializer = BalancePaidSerializer(balance_q)
        amount = serializer.data['amount']
        payment = serializer.data['payment']
        if not payment:
            user = CustomUser.objects.filter(id=serializer.data['user']).first()
            user.rub += Decimal(amount)
            user.save()
            balance_q.payment = True
            balance_q.link_uuid = None
            balance_q.save()

        return Response({'message': 'успешно'}, status=200)



