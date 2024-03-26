# Spotify to YouTube Music Playlist Migration

## Introduction
This Python script helps migrate  playlists from Spotify to YouTube Music. It utilizes the Spotipy library for Spotify API access and the ytmusicapi for YouTube Music interaction. 

## Requirements
- Python 3.x
- Spotipy library
- ytmusicapi library

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install Spotipy library by running `pip install spotipy` in your terminal.
3. Install ytmusicapi library by running `pip install ytmusicapi` in your terminal. (Note: this is an unofficial library, there is currently no public api availablefor 
   ytmusic)

## Setup
1. Obtain Spotify Developer credentials  by creating an application at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Set up environment variables for the Spotify client id and client secret:
    ```
    export SPOTIPY_CLIENT_ID='your-spotify-client-id'
    export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
    ```
    (in main.py these are hardcoded into the program)
3. Run `ytmusicapi oauth` in your terminal and follow the authentication steps to generate an oauth.json file for YouTube Music API access.

## Usage
1. Populate the `p_ids` list in the script with the Playlist IDs of the Spotify playlists you wish to migrate.
2. Enter your Spotify username in the `username` variable. (Not your display name)
3. Run the script. It will fetch tracks from the specified Spotify playlists and create corresponding playlists in YouTube Music, adding the tracks to them.
4. Tracks that fail to add will be displayed in the python console

## Note
- The script may take some time to execute, especially when fetching tracks from large playlists.
- Since YouTube Music does not have an official public API, the script utilizes the unofficial ytmusicapi, which may have limitations or changes over time.

## Disclaimer
This script is provided as-is and may require adjustments based on changes to Spotify, YouTube Music, or the modules used above. Use at your own risk.
