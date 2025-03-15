import regex as re
from bs4 import BeautifulSoup
import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

url_billboard = "https://www.billboard.com/charts/hot-100/2000-08-12"

def verify_date():
    while True:
        year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        if re.match(r"^\d{4}-\d{2}-\d{2}$", year):
            return year
        print("Invalid date format. Please try again.")

def get_songs():
    response = requests.get(url_billboard, headers=header)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    songs = soup.select("li ul li h3")
    return [i[1].text.strip() for i in enumerate(songs) if i[0] < 100]

print(get_songs())

