from rest_framework import serializers
from .models import InterestForm, ProductStats
from decimal import Decimal

class InterestFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestForm
        fields = ["id", "name", "email", "product", "created_at"]
    
    def create(self, validated_data):
        return InterestForm.objects.create(**validated_data)
    

class ProductStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStats
        fields = ["id", "product", "volume", "last", "high", "low"]
        extra_kwargs = {
            "last": {"read_only": True},
            "volume": {"read_only": True},
            "high": {"read_only": True}, 
            "low": {"read_only": True} 
        }

    def to_internal_value(self, data):
        # Convert string values to Decimal where necessary
        internal_data = super().to_internal_value(data)
        try:
            internal_data['volume'] = Decimal(data.get('volume', '0'))
            internal_data['last'] = Decimal(data.get('last', '0'))
            internal_data['high'] = Decimal(data.get('high', '0'))
            internal_data['low'] = Decimal(data.get('low', '0'))
        except ValueError as e:
            raise serializers.ValidationError(f"Invalid numeric value: {e}")

        return internal_data

    def create(self, validated_data):
        return ProductStats.objects.create(**validated_data)