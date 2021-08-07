# Client id:
# 9535173dce7c4a5d8049be9aeeb229ba

# Client secret:
# da4752c48d0d4b508ed2421fd409c27a

import os
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '9535173dce7c4a5d8049be9aeeb229ba'
CLIENT_SECRET = 'da4752c48d0d4b508ed2421fd409c27a'

token = spotipy.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
cache_token = token.get_access_token()
sp = spotipy.Spotify(cache_token)
