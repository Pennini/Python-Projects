import requests as req
import os
from dotenv import load_dotenv

class FlightData:
    def __init__(self) -> None:
        self.url = "https://api.tequila.kiwi.com/"
        self.headers = {
            "apikey": os.getenv("FLIGHT_API")
        }

    def get_iata(self, flight):
        url_iata = self.url + "/locations/query"
        body = {
            "term": flight["city"]
        }
        flight["iataCode"] = "BIFE ACEBOLADO"
        return flight