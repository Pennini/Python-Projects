from bs4 import BeautifulSoup
import requests as req
from pprint import pprint

# with open('./website.html') as web:
#     content = web.read()

# soup = BeautifulSoup(content, 'html.parser')

# print(soup.title)

def get_points(article):
    try:
        soup.find("span", id=f"score_{article.get('id')}").getText().split()[0]
    except AttributeError:
        print(soup.find("span", id=f"score_{article.get('id')}"))

url = "https://news.ycombinator.com/"
response = req.get(url=url)
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

articles = soup.find_all("span", class_="titleline")
votes = soup.find_all('span', class_='score')

votes_num = [int(upvotes.getText().split()[0]) for upvotes in votes]

articles_title = []
articles_links = []

for article in articles:
    articles_title.append(article.find('a').getText())
    articles_links.append(article.find('a').get("href"))

index_most = votes_num.index(max(votes_num))

print(articles_title[index_most], "\n\tLink: ", articles_links[index_most], "\n\tVotes: ", votes_num[index_most])
