from datetime import datetime
from decimal import Decimal as D
import json
import requests

from django.core.management.base import BaseCommand, CommandError
from weather.models import UserCity, Weather

'''Todo: Separate functionality into separate package for use in views'''

OWM_GROUP_URL = 'http://api.openweathermap.org/data/2.5/group?id=%s&units=metric&appid=%s'
API_KEY = '4cecec9258c64eba10ca7090fb68e8e6'

class Command(BaseCommand):
    help = 'Updates the weather data for all cities followed by a user'

    def handle(self, *args, **options):
        ucs = UserCity.objects.order_by('city').distinct('city')

        if len(ucs) == 0:
            return

        ids_str = ','.join([str(uc.city.open_weather_id) for uc in ucs])
        resp = requests.get(OWM_GROUP_URL % (ids_str, API_KEY))
        cities_weather = json.loads(resp.text)['list']

        for cw in cities_weather:
            print('Getting weather for OWM City ID: %s' % cw['id'])
            Weather.objects.create(
                city=ucs.get(city__open_weather_id=cw['id']).city,
                title=cw['weather'][0]['main'],
                description=cw['weather'][0]['description'],
                temp=D(cw['main']['temp']),
                max_temp=D(cw['main']['temp_max']),
                min_temp=D(cw['main']['temp_min']),
                pressure=D(cw['main']['pressure']),
                wind_speed=D(cw['wind']['speed']),
                wind_direction=D(cw['wind'].get('deg', '0')),
                clouds=D(cw['clouds']['all']),
                calculated=datetime.fromtimestamp(cw['dt'])
            )
