import requests as req
import os
from dotenv import load_dotenv

load_dotenv("../../../.env")
class DataManager:
    def __init__(self) -> None:
        self.url = "https://api.sheety.co/844515d1462dff6fdd850525984cc085/flightDeals/prices"
        self.headers = {
            "Authorization": os.getenv("SHEETS_TOKEN")
        }
    
    def get_data(self):
        response = req.get(url=self.url, headers=self.headers)
        response.raise_for_status()
        data = response.json()["prices"]
        return data
    
    def update_table(self, info):
        url_put = self.url + f"/{info["id"]}"
        del info["id"]
        body = {
            "price": info
        }
        response = req.put(url=url_put, headers=self.headers, json=body)
        response.raise_for_status()
        return "Success"