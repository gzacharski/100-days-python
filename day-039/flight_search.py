import requests
import os

API_KEY = os.environ["KIWI_TEQUILA_API_KEY"]
URL = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """

    def __init__(self, departure_city: str = ""):
        self.departure_city = departure_city

    def search_iata_code(self):
        response = requests.get(url=URL, params={"term": self.departure_city}, headers={"apikey": API_KEY})
        return response.json()["locations"][0]["code"]
