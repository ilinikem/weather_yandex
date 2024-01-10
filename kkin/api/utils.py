import requests
from django.conf import settings


def get_coordinates(city_name):
    """Получаем координаты города по названию."""
    api_key = settings.API_KEY_YANDEX_GEOCODE
    geocode_url = ('https://geocode-maps.yandex.ru/1.x/?'
                   f'apikey={api_key}&format=json&geocode={city_name}')

    try:
        response = requests.get(geocode_url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException:
        return None

    try:
        coordinates_str = (
            data['response']['GeoObjectCollection']
            ['featureMember'][0]['GeoObject']['Point']['pos'])
        lat, lon = map(float, coordinates_str.split())
        find_city_name = (
            data['response']['GeoObjectCollection']
            ['featureMember'][0]['GeoObject']['name'])
        return lat, lon, find_city_name
    except (KeyError, ValueError, IndexError):
        return None
