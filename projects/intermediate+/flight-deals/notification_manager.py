import os
from dotenv import load_dotenv
try:
    from twilio.rest import Client
    client = Client(account_sid, auth_token)
except ModuleNotFoundError:
    pass
import smtplib

load_dotenv("../../../.env")

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

class NotificationManager:
    
    def send_sms(self, flight_data):
        message = client.messages.create(
            from_= os.getenv("TWILIO_PHONE"),
            body=f"LOW PRICE!\n{flight_data.origin_city} -> {flight_data.destination_city}:\nPrice: {flight_data.price}\nDate:\n    Departure:\n        Local: {flight_data.out_date}\n    Return:\n        Local: {flight_data.return_date}",
            to= os.getenv("MY_PHONE"),
        )
        print(f"{message} send Succesful")

    def send_emails(self, flight_data, emails):
        data = str(flight_data)
        username = os.getenv('GMAIL_TESTE')
        password = os.getenv('GMAIL_TESTE_PASS')
        
        with smtplib.SMTP('smtp.gmail.com: 587') as conn:
            conn.starttls()
            conn.login(user=username, password=password)
            for email in emails:
                conn.sendmail(from_addr=username, to_addrs=email["email"], msg=f"Subject: Fligth LOW PRICE\n\n{data}".encode('utf-8'))



