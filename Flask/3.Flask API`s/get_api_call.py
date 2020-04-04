#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################    

import requests
import json


#provide your url

url=('http://mapps.cricbuzz.com/cbzios/match/livematches')
#for get_api.py
#url=('http://localhost:5000/2/4)
headers = {'Content-type': 'application/json'}







r = requests.get(url, headers=headers)

print(r.status_code)
a= (r.json())
print(a['matches'])
