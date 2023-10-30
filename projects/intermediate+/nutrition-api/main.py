import requests
from dotenv import load_dotenv, dotenv_values
import os
import datetime as dt

load_dotenv(r'../../../.env')
today = dt.datetime.now()

headers = {
    "x-app-key": os.getenv("NUTRITION_KEY"),
    "x-app-id": os.getenv('NUTRITION_ID')
}

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

body = {
 "query": "Ran 2 miles", # input("Tell me which exercises you did? "),
 "gender": "male",
 "weight_kg": 74,
 "height_cm": 171,
 "age": 22
}

response = requests.post(url=url, headers=headers, json=body)
response.raise_for_status()
data = response.json()["exercises"][0]

url_sheets = "https://api.sheety.co/844515d1462dff6fdd850525984cc085/workoutTracking/workouts"

headers_sheets = {
    "Authorization": os.getenv("NUTRITION_TOKEN")
}

row_sheets = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": data["name"].title(),
        "duration": str(data["duration_min"]),
        "calories": str(data["nf_calories"])
    }
}


response_sheets = requests.post(url=url_sheets, json=row_sheets, headers=headers_sheets)
response_sheets.raise_for_status()


