##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas as pd
import csv
from tkinter import *
from tkinter import messagebox

username = ""
password = ""

current_day = dt.datetime.now().day
current_month = dt.datetime.now().month

data = pd.read_csv("birthdays.csv")

def add_birthday():
    column = ["name", "email", "year", "month", "day"]
    info = [name, email, year, month, day]
    person = {}
    for col, i in zip(column, info):
        person[col] = i.get()
        if person[col] == "":
            messagebox.showinfo(title=f"Error", message=f"{col} data is missing")
            return
        
    with open("birthdays.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=column)
        writer.writerow(person)

def send_email():
    for index, row in data.iterrows():
        if row["month"] == current_month and row["day"] == current_day:
            letter = random.randint(1,3)
            
            with open(f"letter_templates/letter_{letter}.txt", "r") as file:
                message = file.read()
                message = message.replace("[NAME]", row["name"])

            with smtplib.SMTP('smtp.gmail.com: 587') as conn:
                conn.starttls()
                conn.login(user=username, password=password)
                conn.sendmail(from_addr=username, to_addrs=row["email"], msg=f"Subject:Happy Birthday\n\n{message}".encode("utf-8"))


window = Tk()
window.title("Birthday Wisher")
window.config(padx=50, pady=50)

name_label = Label(text="Name: ")
name_label.grid(column=0, row=0, pady=2)
name = Entry(width=40)
name.grid(column=1, row=0, pady=2)

email_label = Label(text="Email: ")
email_label.grid(column=0, row=1, pady=2)
email = Entry(width=40)
email.grid(column=1, row=1, pady=2)

year_label = Label(text="Year: ")
year_label.grid(column=0, row=2, pady=2)
year = Entry(width=40)
year.grid(column=1, row=2, pady=2)

month_label = Label(text="Month: ")
month_label.grid(column=0, row=3, pady=2)
month = Entry(width=40)
month.grid(column=1, row=3, pady=2)

day_label = Label(text="Day: ")
day_label.grid(column=0, row=4, pady=2)
day = Entry(width=40)
day.grid(column=1, row=4, pady=2)

button_add = Button(text="Add", command=add_birthday)
button_add.grid(column=1, row=5, pady=5, padx=5)
button_send = Button(text="Send email", command=send_email)
button_send.grid(column=1, row=6, pady=5, padx=5)

window.mainloop()



