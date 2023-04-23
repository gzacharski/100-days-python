# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from constants import URL, HEADERS
from data_manager import DataManager
from pprint import pprint

response = requests.get(url=URL, headers=HEADERS)
sheet_data = response.json().get("prices")

for row in sheet_data:
    iata_code: str = row.get("iataCode")
    if iata_code is None or len(iata_code) == 0:
        departure_city = row["city"]
        iata_code = FlightSearch(departure_city).search_iata_code()
        row["iataCode"] = iata_code
        dm = DataManager(row)
        dm.update_row()

response = requests.get(url=URL, headers=HEADERS)
sheet_data = response.json().get("prices")
pprint(sheet_data)
