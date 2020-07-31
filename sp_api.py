import json
import os
import requests
from datetime import datetime
from base64 import b64encode
# custom functions
import config

def get_artist_id(token,artist,market):
    artist = artist.replace(" ","%20")
    query = config.endpoints['search'] + 'q=' + artist + "&type=artist&market=" + market
    header = config.endpoints['header']
    header['Authorization'] = "Bearer " + token
    response = requests.get(query, headers = header)
    artist_id = response.json()['artists']['items'][0]['id']
    return artist_id

def get_top_tracks(token,artist,market):
    artist_id = get_artist_id(token,artist,market)
    query = config.endpoints['topTracks'].replace("ARTIST_ID",artist_id) + 'country=' + market
    header = config.endpoints['header']
    header['Authorization'] = "Bearer " + token
    response = requests.get(query, headers = header)
    print(artist.title())
    print('mercado: {}'.format(market))
    track_position = 1
    for t in response.json()['tracks']:
        #print('faixa: {} / album: {} / popularidade {}'.format(t['name'],t['album']['name'],t['popularity']))
        print('{} - {} - {}'.format(track_position, t['name'],t['album']['name']))
        track_position += 1