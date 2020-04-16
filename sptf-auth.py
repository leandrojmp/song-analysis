import json
import requests
from base64 import b64encode

config = json.load(open('conf/secrets.json','r'))

endpointAuth = "https://accounts.spotify.com/api/token"
clientAuth = config['clientId'] + ":" + config['clientSecret']
headerAuth = { "Authorization": "Basic " + b64encode(clientAuth.encode('utf-8')).decode('utf-8') } 
bodyAuth = { "grant_type": "client_credentials" } 

auth = requests.post(endpointAuth, data = bodyAuth, headers = headerAuth)
