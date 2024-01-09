from datetime import timedelta

import requests
from django.conf import settings
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.response import Response

from weather.models import Weather

from .serializers import GetWeatherSerializer
from .utils import get_coordinates


class GetWeatherViewSet(viewsets.ViewSet):
    """Получение погоды от Яндекс Погоды."""
    api_key = settings.API_KEY_YANDEX_WEATHER
    endpoint = 'https://api.weather.yandex.ru/v1/informers'

    def list(self, request):
        city_name = request.query_params.get('city')
        if not city_name:
            return Response({'error': 'Обязательный параметр "city"'},
                            status=status.HTTP_400_BAD_REQUEST)

        formatted_city_name = city_name.title()
        coordinates = get_coordinates(formatted_city_name)
        lon, lat, find_city_name = coordinates

        try:
            weather_record = Weather.objects.get(city_name=find_city_name)
            if (weather_record.updated_date + timedelta(minutes=30)
                    > timezone.now()):
                serializer = GetWeatherSerializer(weather_record)
                return Response(serializer.data)
            else:
                # Если запись старше 30 минут, обновляем информацию о погоде
                api_url = (f'{self.endpoint}?&lat={weather_record.latitude}'
                           f'&lon={weather_record.longitude}')

                try:
                    headers = {'X-Yandex-API-Key': self.api_key}
                    response = requests.get(api_url, headers=headers)
                    response.raise_for_status()
                    data = response.json()
                except requests.exceptions.RequestException as e:
                    return Response(
                        {'error': f'Yandex Weather API: {str(e)}'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                try:
                    fact = data['fact']
                    # Обновляем данные в существующей записи
                    weather_record.temperature = fact['temp']
                    weather_record.pressure = fact['pressure_mm']
                    weather_record.wind_speed = fact['wind_speed']
                    weather_record.updated_date = timezone.now()
                    weather_record.save()

                    serializer = GetWeatherSerializer(weather_record)
                    return Response(serializer.data)

                except KeyError:
                    return Response(
                        {
                            'error': 'Неверный запрос Yandex Weather API'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Weather.DoesNotExist:
            if not coordinates:
                return Response(
                    {'error': f'Не удалось определить координаты'
                              f' для города {find_city_name}'},
                    status=status.HTTP_400_BAD_REQUEST)

            # lon, lat, city_name = coordinates
            api_url = f'{self.endpoint}?&lat={lat}&lon={lon}'

            try:
                headers = {'X-Yandex-API-Key': self.api_key}
                response = requests.get(api_url, headers=headers)
                response.raise_for_status()
                data = response.json()
            except requests.exceptions.RequestException as e:
                return Response({'error': f'Yandex Weather API: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            try:
                fact = data['fact']
                weather_data = {
                    'city_name': find_city_name,
                    'latitude': lat,
                    'longitude': lon,
                    'temperature': fact['temp'],
                    'pressure': fact['pressure_mm'],
                    'wind_speed': fact['wind_speed'],
                }
                serializer = GetWeatherSerializer(data=weather_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors,
                                    status=status.HTTP_400_BAD_REQUEST)

            except KeyError:
                return Response({'error': 'Неверный запрос'
                                          ' Yandex Weather API'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
