import regex as re

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

def verify_date():
    while True:
        year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        if re.match(r"^\d{4}-\d{2}-\d{2}$", year):
            return year
        print("Invalid date format. Please try again.")

