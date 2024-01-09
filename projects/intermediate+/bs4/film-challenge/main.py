import requests as req
from bs4 import BeautifulSoup
import random

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = req.get(URL)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")

movies = soup.find_all('h3', class_="title")

with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies[::-1]:
        writer = file.write(f"{movie.getText()}\n")

movie_list = random.choice(movies).getText().split()[1:]
print(" ".join(movie_list))