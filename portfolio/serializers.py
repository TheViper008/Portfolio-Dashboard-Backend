from rest_framework import serializers

class HoldingSerializer(serializers.Serializer):
    symbol = serializers.CharField()
    name = serializers.CharField()
    quantity = serializers.IntegerField()
    avgPrice = serializers.FloatField()
    currentPrice = serializers.FloatField()
    sector = serializers.CharField()
    marketCap = serializers.CharField()
    value = serializers.FloatField()
    gainLoss = serializers.FloatField()
    gainLossPercent = serializers.FloatField()