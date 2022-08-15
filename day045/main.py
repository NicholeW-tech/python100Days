import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
movie_webpage = response.text
soup = BeautifulSoup(movie_webpage, "html.parser")
movie_data = soup.findAll(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movie_data]

print(movie_titles)
