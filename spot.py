import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import language
import tweets

client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                      client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_playlists():
    featured_playlist = sp.featured_playlists(locale='en', country='CA', limit=30)
    list_of_playlists = [[]]
    for playlist in featured_playlist:

        percentage = abs(((language.sentiment(tweets.get_timeline()) - language.sentiment(
            playlist['name'])) / language.sentiment(playlist['name'])))
        if percentage <= 15:
            list_of_playlists.append(playlist)

    return list_of_playlists


def main():
    get_playlists()


if __name__ == '__main__':
    main()
