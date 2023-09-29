import requests

url = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(url)
response.raise_for_status()
question_data = response.json()["results"]
