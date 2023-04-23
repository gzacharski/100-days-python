import requests
from constants import URL, HEADERS


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, row: dict):
        self.row = row

    def update_row(self):
        row_id = self.row["id"]
        response = requests.put(url=f"{URL}/{row_id}", headers=HEADERS, json={"price": self.row})
        return response.json()
