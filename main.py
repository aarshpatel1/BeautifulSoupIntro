from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
html_code = response.text

soup = BeautifulSoup(html_code, "html.parser")
print(soup.prettify())

movie_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
pprint(movie_titles)

ordered_movie_titles = [movie_titles[i] for i in range(len(movie_titles) - 1, -1, -1)]
pprint(ordered_movie_titles)

with open("movie.txt", "w", encoding="utf-8") as movie_names:
    for movie in ordered_movie_titles:
        movie_names.write(f"{movie}\n")
