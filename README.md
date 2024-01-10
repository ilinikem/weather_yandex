# weather_yandex

Этот проект предоставляет API для запроса погоды от Яндекс Погоды. При запросе информацию о городе использует API YANDEX GEOCODE для получения координат города. Имеет БД для хранения информации о городе. При повторном запросе к одному и тому же городу в течение 30 минут, будет отдаваться информация из БД.

## Установка и использование

1. **Клонирование репозитория:**

   ```git clone git@github.com:ilinikem/weather_yandex.git```
   ```cd ваш_репозиторий```


1. Установите зависимости:

   ```pip install -r requirements.txt```

2. Создайте файл .env в корне проекта и укажите в нем необходимые настройки:

## Ключи
- SECRET_KEY
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB
- DB_NAME
- DB_HOST
- DB_PORT
- API_KEY_YANDEX_GEOCODE
- API_KEY_YANDEX_WEATHER
   
3. Создайте файл .env в корне проекта и укажите в нем необходимые настройки:

   ```python manage.py makemigrations```
   ```python manage.py migrate```

4. Запустите сервер::

   ```python manage.py runserver```

## Зависимости
- asgiref==3.7.2
- certifi==2023.11.17
- charset-normalizer==3.3.2
- Django==5.0.1
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.3.1
- flake8==6.0.0
- flake8-isort==6.0.0
- idna==3.6
- isort==5.13.2
- mccabe==0.7.0
- psycopg2==2.9.9
- pycodestyle==2.10.0
- pyflakes==3.0.1
- PyJWT==2.8.0
- python-dotenv==1.0.0
- pytz==2023.3.post1
- requests==2.31.0
- setuptools==69.0.3
- sqlparse==0.4.4
- urllib3==2.1.0


## Лицензия
Этот проект лицензирован по BSD 3-Clause License.



## Использование API

### Получение погоды для города:

Отправьте GET-запрос на `/api/weather/` с параметром `city`, чтобы получить информацию о погоде для указанного города.

**Пример:**

```http://127.0.0.1:8000/api/weather/?city=Москва```

**Ответ:**


```json
{
    "city_name": "Москва",
    "temperature": -2,
    "pressure": 760,
    "wind_speed": 5
}

