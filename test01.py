# Client id:
# 9535173dce7c4a5d8049be9aeeb229ba

# Client secret:
# da4752c48d0d4b508ed2421fd409c27a

import os
import sys
import spotipy
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Setting the environment variables and getting Spotify's authentication
os.environ['SPOTIPY_CLIENT_ID'] = '9535173dce7c4a5d8049be9aeeb229ba'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'da4752c48d0d4b508ed2421fd409c27a'

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


class Spotify():

    def __init__(self):
        pass

    def search_artist(self, artist_name):
        if len(sys.argv) > 1:
            name = ' '.join(sys.argv[1:])
        else:
            name = artist_name

        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        for i in range(5):
            try:
                print(items[i])
            except:
                print("error")

    def search_songs(self, song_name):
        name = song_name
        results = spotify.search(q='track:' + name, type='track')
        items = results['tracks']['items']
        for item in items:
            print(item)
            print('\nArtist : ' + item['album']['artists'][0]['name'])
            print('Preview URL : ' + str(item['preview_url']))
            print('ID : ' + str(item['id']))
            print('API : '+ str(item['href']))
            print('URL : '+ str(item['external_urls']['spotify']))
            # webbrowser.open(item['external_urls']['spotify'])
            # return


if __name__ == "__main__":
    s1 = Spotify()
    s1.search_artist("selena gomez")
    #s1.search_songs("Common People")
