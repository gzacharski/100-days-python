import requests
import json
from twilio.rest import Client
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

params = {
    "lat": 45.326908,
    "lon": 14.441000,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=params)
response.raise_for_status()
weather_data = json.dumps(response.json(), indent=2)

weather_response = response.json()
weather_list = [weather for weather in weather_response.get("list")[:12] if weather.get("weather")[0].get("id") < 700]
if len(weather_list) > 1:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring umbrella", from_="+15074146919",
                                     to="+48665762682")
    print(message.status)
