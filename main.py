import html
from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
html_code = response.text

soup = BeautifulSoup(html_code, "html.parser")

movie_titles = [html.unescape(title.getText()) for title in soup.find_all(name="h3", class_="title")]
pprint(movie_titles)

with open("movie.txt", "w", encoding="utf-8") as movie_names:
    for i in range(len(movie_titles) + 1):
        movie_names.write(f"{movie_titles[-i]}\n")
