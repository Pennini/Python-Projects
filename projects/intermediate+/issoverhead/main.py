import requests
from datetime import datetime
import time
import smtplib

MY_LAT = -23.550520 
MY_LONG = -46.633308

def compare_positions():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG <= iss_longitude + 5):
        return True 
    else:
        return False

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset <= time_now or time_now <= sunrise:
        return True
    else:
        return False

def send_email():
    
    username = ""
    password = ""
    
    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.login(username, password)
        conn.starttls()
        conn.sendmail(username, username, msg="Subject: ISS\n\n Look up!")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if compare_positions() and is_night():
        send_email()
    time.sleep(60)


