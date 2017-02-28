from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=12, decimal_places=8)
    lon = models.DecimalField(max_digits=12, decimal_places=8)
    country_code = models.CharField(max_length=2)
    open_weather_id = models.IntegerField()
