import requests
from datetime import datetime as dt
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

SHEETY_URL = os.environ["SHEETY_URL"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise = input("Tell me which exercise you did: ")

body = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 75.5,
    "height_cm": 183.64,
    "age": 30
}

response = requests.post(url=URL, headers=HEADERS, json=body)

for exercise in response.json().get("exercises"):
    today_date = dt.now().strftime("%d/%m/%Y")
    now_time = dt.now().strftime("%X")
    body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise.get("name").title(),
            "duration": exercise.get("duration_min"),
            "calories": exercise.get("nf_calories"),
        }
    }
    sheety_response = requests.post(
        url=SHEETY_URL,
        headers={"Authorization": ACCESS_TOKEN, "Content-Type": "application/json"},
        json=body)

    print(sheety_response.text)
