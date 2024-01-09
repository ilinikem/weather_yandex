from django.db import models


class Weather(models.Model):
    city_name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Название города',
        help_text='Введите название города',
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создание записи',
        help_text='Создается автоматически. Дата и время создания записи',
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время обновления записи',
        help_text='Обновляется автоматически. Дата и время обновления записи'
    )
    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Температура',
        help_text='Текущая температура в градусах Цельсия',
    )
    pressure = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Давление',
        help_text='Атмосферное давление в мм рт. ст.',
    )
    wind_speed = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Скорость ветра',
        help_text='Скорость ветра в м/с',
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='Широта',
        help_text='Координата широты города',
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='Долгота',
        help_text='Координата долготы города',
    )

    class Meta:
        verbose_name = 'Погода'
        verbose_name_plural = 'Погода в городах'

    def __str__(self):
        return (f"{self.city_name}, Температура: {self.temperature},"
                f" Давление: {self.pressure},"
                f" Скорость ветра: {self.wind_speed}")
