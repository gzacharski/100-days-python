import requests
import datetime as dt

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = ""
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_ID = ""
graph_config = {
    "id": graph_ID,
    "name": "Climbing Gym graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)
today = dt.datetime.today().strftime("%Y%m%d")
data = {"date": today, "quantity": "10"}
# response = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_ID}", headers=headers, json=data)
# print(response.text)

# response = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_ID}/{today}", headers=headers,
#                         json={"quantity": "10"})
# print(response.text)

response = requests.delete(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_ID}/{today}", headers=headers)
print(response.text)
