import json
import os
import requests
from sys import argv
from datetime import datetime
from base64 import b64encode
# custom functions
import config
import spoauth
import sp_api

args = config.parser.parse_args()

token = spoauth.renew_token()
artist = args.a
market = args.m
sp_api.get_top_tracks(token,artist,market)