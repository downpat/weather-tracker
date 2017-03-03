from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=12, decimal_places=8)
    lon = models.DecimalField(max_digits=12, decimal_places=8)
    country_code = models.CharField(max_length=2)
    open_weather_id = models.IntegerField()

class UserCity(models.Model):
    city = models.ForeignKey(City)
    user = models.ForeignKey(User)

class TempRange(models.Model):
    email_notification = models.BooleanField(default=False)
    max_temp = models.DecimalField(max_digits=7, decimal_places=3)
    min_temp = models.DecimalField(max_digits=7, decimal_places=3)
    user_city = models.ForeignKey(UserCity)

class Weather(models.Model):
    city = models.ForeignKey(City)
    title = models.CharField(max_length=200)
    description = models.TextField()
    temp = models.DecimalField(max_digits=7, decimal_places=3)
    max_temp = models.DecimalField(max_digits=7, decimal_places=3)
    min_temp = models.DecimalField(max_digits=7, decimal_places=3)
    pressure = models.DecimalField(max_digits=9, decimal_places=3)
    wind_speed = models.DecimalField(max_digits=7, decimal_places=3)
    wind_direction = models.DecimalField(max_digits=7, decimal_places=3)
    clouds = models.DecimalField(max_digits=5, decimal_places=2)
    calculated = models.DateTimeField()
    retrieved = models.DateTimeField(auto_now_add=True)
    
class Notification(models.Model):
    weather = models.ForeignKey(Weather)
    temp_range = models.ForeignKey(TempRange)
    user = models.ForeignKey(User)
    unread = models.BooleanField(default=True)
