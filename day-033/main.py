import requests
from datetime import datetime

MY_LATITUDE = 51.507351
MY_LONGITUDE = -0.127758

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
print(response.json())

parameters = {
    "lat": MY_LATITUDE,
    "long": MY_LONGITUDE,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())
sunrise = response.json()["results"]["sunrise"]
print(sunrise)
print(sunrise.split("T"))

time_now = datetime.now()
print(time_now)
