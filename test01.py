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

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
