import json
import os
import requests
from sys import argv
from datetime import datetime
from base64 import b64encode
# custom functions
import config
import sptf_oauth
import sptf_api

args = config.parser.parse_args()

token = sptf_oauth.renew_token()
artist = args.a
market = args.m
sptf_api.get_top_tracks(token,artist,market)