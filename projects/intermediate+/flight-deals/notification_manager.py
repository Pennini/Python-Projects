import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("../../../.env")

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

client = Client(account_sid, auth_token)
class NotificationManager:
    
    def send_sms(self, flight_data):
        message = client.messages.create(
            from_= os.getenv("TWILIO_PHONE"),
            body=f"LOW PRICE!\n{flight_data.origin_city} -> {flight_data.destination_city}:\nPrice: {flight_data.price}\nDate:\n    Departure:\n        Local: {flight_data.out_date}\n    Return:\n        Local: {flight_data.return_date}",
            to= os.getenv("MY_PHONE"),
        )
        print(f"{message} send Succesful")
