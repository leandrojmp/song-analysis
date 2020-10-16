import json
import os
import requests
from datetime import datetime
from base64 import b64encode
# custom functions
import config

def check_token_expiration():
    """ Check if the token has expired, returns 0 if expired or the token if not expired """    
    try:
        with open(config.paths['conf_dir'] + 'auth.token','r') as token_file:
            token = token_file.read().strip('\n').split(':')
            token_time = datetime.now() - datetime.strptime(token[0],'%Y%m%d%H%M%S%f')
            if token_time.seconds > 3500:
                return 0
            else:
                return token[1]
    except FileNotFoundError:
        return 0

def get_auth_token():
    """ Get the OAuth token and stores into a local file """
    token_endpoint = "https://accounts.spotify.com/api/token"
    client = config.config['clientId'] + ":" + config.config['clientSecret']
    header = { "Authorization": "Basic " + b64encode(client.encode('utf-8')).decode('utf-8') } 
    body = { "grant_type": "client_credentials" } 
    response = requests.post(token_endpoint, data = body, headers = header)
    auth_token = response.json()['access_token']
    token_hash =  datetime.strftime(datetime.now(), '%Y%m%d%H%M%S%f') + ":" + auth_token
    with open(config.paths['conf_dir'] + 'auth.token','w') as token_file:
        token_file.write(token_hash + '\n')
    return auth_token

def renew_token():
    """ Check if the token is still valid, if not, renews it, returns a valid token """
    token = check_token_expiration()
    if token == 0:
        new_token = get_auth_token()
        return new_token
    else:
        return token