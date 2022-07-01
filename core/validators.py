from rest_framework import serializers

def validate_amount( value):
    if int(value) <0:
        raise serializers.ValidationError(f"amount can't have a negative value and you input {value}")
    return value