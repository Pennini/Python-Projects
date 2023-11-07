import requests as req
import os
from dotenv import load_dotenv

load_dotenv("../../../.env")
class DataManager:
    def __init__(self) -> None:
        self.url = "https://api.sheety.co/844515d1462dff6fdd850525984cc085/flightDeals/prices"
        self.url_users = "https://api.sheety.co/844515d1462dff6fdd850525984cc085/flightDeals/users"
        self.headers = {
            "Authorization": os.getenv("SHEETS_TOKEN")
        }
    
    def get_data(self):
        response = req.get(url=self.url, headers=self.headers)
        response.raise_for_status()
        data = response.json()["prices"]
        return data
    
    def update_table(self, info):
        url_put = self.url + f"/{info['id']}"
        del info["id"]
        body = {
            "price": info
        }
        response = req.put(url=url_put, headers=self.headers, json=body)
        response.raise_for_status()
        return "Success"
    

    def add_person(self):
        print("Welcome to André's Flight Club!")
        f_name = input("What is your first name? ")
        l_name = input("What is your last name? ")
        email = input("What is your email? ")
        email_confirm = input("Type your email again: ")
        if email != email_confirm:
            print("Emails don't match. Try again.")
            return
        else:
            body = {
                "user": {
                    "firstName": f_name,
                    "lastName": l_name,
                    "email": email
                }
            }
            response = req.post(url=self.url_users, json=body, headers=self.headers)
            response.raise_for_status()
            print("Success! You're in the club!")


    def get_emails(self):
        response = req.get(url=self.url_users, headers=self.headers)
        response.raise_for_status()
        data = response.json()["users"]
        return data
