from datetime import date

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

CLIENT_ID = CLIENT_ID
CLIENT_SECRET = SECRET

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               show_dialog=True,
                                               cache_path="token.txt"))


user_id = sp.current_user()["id"]

user_input = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

url = f"https://www.billboard.com/charts/hot-100/{user_input}"
response = requests.get(url)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

# song_titles = soup.findAll(name="h3", class_="c-title", id="title-of-a-story")
song_titles = soup.select("li h3")

# there were multiple classes in the class row and you seperate them by putting a . in front of each not a space
song_artists = soup.select(".c-label.a-font-primary-s")

song_title = [title.getText().replace("\n", "") for title in song_titles]
song_artist = [song.getText().replace("\n", "") for song in song_artists]


song_uris = []
year = user_input.split("-")[0]
for song in song_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
