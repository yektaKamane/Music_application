# Client id:
# 9535173dce7c4a5d8049be9aeeb229ba

# Client secret:
# da4752c48d0d4b508ed2421fd409c27a

import os
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

# Setting the environment variables and getting Spotify's authentication
os.environ['SPOTIPY_CLIENT_ID'] = '9535173dce7c4a5d8049be9aeeb229ba'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'da4752c48d0d4b508ed2421fd409c27a'

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


# The rest is just sth I copied for test

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
