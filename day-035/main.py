import requests
import json

API_KEY = ""

# OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    # "lat": 20.6275,
    "lat": 55.864239,
    # "lon": 50.8703,
    "lon": -4.251806,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=params)
response.raise_for_status()
weather_data = json.dumps(response.json(), indent=2)

weather_response = response.json()
weather_list = [weather for weather in weather_response.get("list")[:12] if weather.get("weather")[0].get("id") < 700]
if len(weather_list) > 1:
    print("Bring an Umbrella")
