from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    location = serializers.CharField(max_length=100)