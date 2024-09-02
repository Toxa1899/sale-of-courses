from rest_framework import serializers

from applications.balance.models import Balance


class BalancePaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['amount']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['user'] = user
        return Balance.objects.create(**validated_data)