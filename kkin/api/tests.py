from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
from rest_framework.test import APIClient

from .utils import get_coordinates


class WeatherAPITestCase(TestCase):
    def setUp(self):
        self.api_client = APIClient()

#     def test_get_weather(self):
#         """Тест получения информации о погоде для валидного города."""
#         response = self.api_client.get(
#             reverse('api:weather-list'),
#             {'city': 'Москва'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
    def test_get_coordinates(self):
        """Тест получения координат для валидного города."""
        coordinates = get_coordinates('Москва')
        self.assertIsNotNone(coordinates)
        self.assertIsInstance(coordinates, tuple)

    # def test_get_coordinates_invalid_city(self):
    #     """Тест получения координат для невалидного города."""
    #     coordinates = get_coordinates('InvalidCity')
    #     self.assertIsNone(coordinates)
