from rest_framework import serializers

from weather.models import Weather


class GetWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['city_name', 'temperature', 'pressure',
                  'wind_speed', 'longitude', 'latitude']
