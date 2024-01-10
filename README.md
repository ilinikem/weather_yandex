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
- API_KEY_YANDEX_GEOCODE
- API_KEY_YANDEX_WEATHER
- BOT_TOKEN

**(Необходимые ключи для деплоя)**
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB
- DB_NAME
- DB_HOST
- DB_PORT   
3. Создайте файл .env в корне проекта и укажите в нем необходимые настройки:

   ```python manage.py makemigrations```
   ```python manage.py migrate```

4. Запустите сервер в первом терминале:

   ```python manage.py runserver```

## Зависимости
- anyio==4.2.0
- asgiref==3.7.2
- certifi==2023.11.17
- charset-normalizer==3.3.2
- Django==5.0.1
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.3.1
- flake8==6.0.0
- flake8-isort==6.0.0
- h11==0.14.0
- httpcore==1.0.2
- httpx==0.25.2
- idna==3.6
- isort==5.13.2
- mccabe==0.7.0
- psycopg2==2.9.9
- pycodestyle==2.10.0
- pyflakes==3.0.1
- PyJWT==2.8.0
- python-dotenv==1.0.0
- python-telegram-bot==20.7
- pytz==2023.3.post1
- requests==2.31.0
- setuptools==69.0.3
- sniffio==1.3.0
- sqlparse==0.4.4
- urllib3==2.1.0




## Использование API

### Получение погоды для города:

Отправьте GET-запрос на `/api/weather/` с параметром `city`, чтобы получить информацию о погоде для указанного города.

**Пример:**

```http://127.0.0.1:8000/api/weather/?city=Москва```

**Ответ:**


```json
{
    "city_name": "Калининград",
    "temperature": "0.00",
    "pressure": "771.00",
    "wind_speed": "6.00",
    "longitude": "20.510137",
    "latitude": "54.710162"
}
```

# Телеграм-бот для получения погоды

Этот телеграм-бот предоставляет информацию о погоде для указанного города. Бот ждем ввода названия города, а потом отправляет запрос на указанный ендпоинт и полученный ответ выводит пользователю.

## Использование
  
1. Запустите бота во втором терминале:

   ```python bot.py```


## Лицензия
Этот проект лицензирован по BSD 3-Clause License.