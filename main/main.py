# This is a python script to migrate playlists from Spotify to YouTube Music
# RD 2024


# Playlist ID's of Spotify playlists. Enter all the playlist id's you need to migrate within the list
p_ids = []

# Spotify username (not your display name)
username = "your-username-goes-here"

# Setup Credentials
# You'll need a Spotify dev account for this - it's free!
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Client id and client secret - you can set as env variable if you like
cid = 'your-spotify-client-id'
secret = 'your-spotify-client-secret'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Get tracks from playlists - this might take a while.
def get_playlist_tracks(username, playlist_id):
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


# Get playlist name
def get_playlist_name(play_id):
    results = sp.user_playlist(user=None, playlist_id=play_id, fields="name")
    return results["name"]


all_info = dict()  # all your playlists and tracks get stored here


# Get all the tracks from playlists - this will take a while
for p_id in p_ids:
    p_name = get_playlist_name(p_id)
    req_info = list()
    all_tracks = get_playlist_tracks(username, p_id)
    all_track_ids = []
    for i in all_tracks:
        all_track_ids.append(i['track']['id'])

    for track_info in all_tracks:
        p_info = dict()
        p_info["track_name"] = track_info['track']['name']
        p_info["artist_name"] = track_info['track']['artists'][0]['name']  # Assuming only one artist per track
        p_info["release_date"] = track_info['track']['album']['release_date']
        req_info.append(p_info)

    all_info[p_name] = req_info

# Now for the fun bit - creating your playlists in YouTube Music
# The tricky bit is that there isn't any official public YouTube Music API
# We'll be using the unofficial ytmusicapi

from ytmusicapi import YTMusic

# After installing the module, run 'ytmusicapi oauth' in terminal and follow steps displayed.
yt = YTMusic('oauth.json')

# Now we create the playlists and add the songs
for playlist in all_info:
    playlistId = yt.create_playlist(playlist, "")
    vid_ids = list()
    for song in all_info[playlist]:
        query = song["artist_name"] + " " + song["track_name"]
        search_result = yt.search(query)
        if 'videoId' in search_result[0]:
            id = search_result[0]['videoId']
            vid_ids.append(id)
        else:
            print("Failed: ", playlist, query) # tracks that fail to gett added are displayed on console

    yt.add_playlist_items(playlistId, vid_ids)

# Wohoo! we did it!!
