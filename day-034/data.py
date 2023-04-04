import requests

TRIVIA_ENDPOINT = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get(TRIVIA_ENDPOINT, params=parameters)
response.raise_for_status()
question_data = response.json().get("results")
