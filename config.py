import json
import os
import argparse

# path configuration
base_path = os.getcwd() 
paths = {
    "conf_dir": base_path + '/conf/'
}

endpoints = {
    "search": "	https://api.spotify.com/v1/search?",
    "newReleases": "https://api.spotify.com/v1/browse/new-releases?",
    "topTracks": "https://api.spotify.com/v1/artists/ARTIST_ID/top-tracks?",
    "header": {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
}
config = json.load(open(paths['conf_dir'] + 'secrets.json','r'))

# parser

parser = argparse.ArgumentParser(description="song-analysis", add_help=False)
 
parser.add_argument (
    '-h',
    '--help',
    action='help',
    default=argparse.SUPPRESS,
    help='exibe mensagem de ajuda e sai'
)
 
parser.add_argument (
    '-m',
    default='BR',
    help='país para pesquisar, ex: BR, US, NL (default: BR)'
)
 
parser.add_argument (
    '-a',
    default = "arcade fire",
    help='nome do artista entre aspas dupla, exemplo "arcade fire"',
)