import json

def owm2django(owm_file_name, django_file_name):
    city_models = []
    counter = 1
    with open(owm_file_name, 'r') as owm_file:
        with open(django_file_name, 'w') as dj_file:
            for city_line in owm_file:
                city = json.loads(city_line)
                city_models.append({
                    "model": "weather.city",
                    "pk": counter,
                    "fields": {
                        "name": city['name'],
                        "lat": city['coord']['lat'],
                        "lon": city['coord']['lon'],
                        "country_code": city['country'],
                        "open_weather_id": city['_id']
                    }
                })
                counter += 1
            dj_file.write(json.dumps(city_models))

if __name__ == "__main__":
    owm2django('city.list.json', 'city.fixture.json')
