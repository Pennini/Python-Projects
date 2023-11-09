import requests as req
import os
from dotenv import load_dotenv
import datetime as dt
from flight_data import FlightData
from pprint import pprint

load_dotenv("../../../.env")


class FlightSearch:
    def __init__(self) -> None:
        self.url = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": os.getenv("FLIGHT_API")
        }
    

    def get_price(self, airport, origin_city_code, from_time, to_time):
        url_search = self.url + "/v2/search"
        body = {
            "fly_from": origin_city_code,
            "fly_to": airport["iataCode"],
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "price_to": airport["lowestPrice"],
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "BRL"
        }
        response = req.get(url=url_search, params=body, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        try:
            data = response.json()["data"][0]
        except IndexError:
            body["max_stopovers"] = 2
            response = req.get(url=url_search, params=body, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {airport['city']}.")
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(flight_data)
                return flight_data
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(flight_data)
        return flight_data
    
    def get_iata(self, flight):
        url_iata = self.url + "/locations/query"
        body = {
            "term": flight["city"],
            "location_types": "city"
        }
        response = req.get(url=url_iata, params=body, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]