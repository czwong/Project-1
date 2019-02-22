import spotipy
import os
import webbrowser
import json
import sys
import spotipy.util as util
from json.decoder import JSONDecodeError
import requests

#Get the username from terminal
username = sys.argv[1]

#user id: sunofalaura?si=k2b6U7prRTSlhE46T48HVg

#erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

#create spotifyobject
spotifyobject = spotipy.Spotify(auth=token)

#prints out json data in a pretty format
#print(json.dumps(VARIABLE, sort_keys=True, indent=4))

user = spotifyobject.current_user()
dispayName= user["display_name"]
followers = user["followers"]["total"]
#print(json.dumps(user, sort_keys=True, indent=4))
"""
try:
    print()
    target_url="https://api.spotify.com/v1/browse/featured-playlists"
    print(requests.get(target_url).json())
except:
    print("Didn't work")
"""

while True:
    print()
    searchQuery = input("Which artist would you like to search for?")
    searchResults = spotifyobject.search(searchQuery,1,0,"artist")
    print(json.dumps(searchResults, sort_keys=True, indent=4))
