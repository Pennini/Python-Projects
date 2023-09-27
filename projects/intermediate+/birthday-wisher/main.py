import smtplib
import datetime as dt
import random

username = ""
password = ""

current_weekday = dt.datetime.now().weekday()

if current_weekday == 1:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)


    with smtplib.SMTP('smtp.gmail.com: 587') as conn:
        conn.starttls()
        conn.login(user=username, password=password)
        conn.sendmail(from_addr=username, to_addrs=username, msg=f"Subject:Motivation\n\n{quote}")
    