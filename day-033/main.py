import time

import requests
from datetime import datetime
import smtplib

MY_LATITUDE = 51.507351
MY_LONGITUDE = -0.127758

MY_EMAIL = ""
PASSWORD = ""
RECIPIENT_EMAIL = ""


# if the ISS is close to my current position
# and it is currently dark
# then send me an email to tell me to look up
# Bonus: run the code every 60 seconds

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT_EMAIL,
                            msg=f"Subject:International Space Station\n\nLook at the sky!")


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    current_latitude = float(iss_response.json()["iss_position"]["latitude"])
    current_longitude = float(iss_response.json()["iss_position"]["longitude"])

    is_near_my_latitude = MY_LATITUDE - 5 <= current_latitude <= MY_LATITUDE + 5
    is_near_my_longitude = MY_LONGITUDE - 5 <= current_longitude <= MY_LONGITUDE + 5
    return is_near_my_latitude and is_near_my_longitude


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "long": MY_LONGITUDE,
        "formatted": 0
    }
    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunrise = datetime.fromisoformat(sun_response.json()["results"]["sunrise"])
    sunset = datetime.fromisoformat(sun_response.json()["results"]["sunset"])
    time_now = datetime.now()
    return time_now.astimezone() < sunrise.astimezone() or sunset.astimezone() < time_now.astimezone()


while True:
    if is_night() and is_iss_overhead():
        send_email()
    else:
        print("no")
    time.sleep(60)
