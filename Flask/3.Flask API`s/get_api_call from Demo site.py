#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################    
# site https://reqres.in/
import requests
import json


#provide your url

#url=('http://mapps.cricbuzz.com/cbzios/match/livematches/')
#for get_api.py
#url=('http://localhost:5000/api/2/4')


url=('https://reqres.in/api/users?page=2')
#Site for demo API
headers = {'Content-type': 'application/json'}







r = requests.get(url, headers=headers)

print(r.status_code)
print(r.json())

