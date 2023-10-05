import requests

url = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "0c86e4e6f6f41e87f7018eebe8b768dd"

parameters = {
    "lat": -23.550520,
    "lon": -46.633308,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()["hourly"]

for hour in data[:12]:
    if int(hour["weather"][0]["id"]) < 700:
        print("It will rain", hour)
        break



