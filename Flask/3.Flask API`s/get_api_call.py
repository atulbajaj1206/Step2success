#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################    

import requests
import json


#provide your url

#url=('http://mapps.cricbuzz.com/cbzios/match/livematches/')
#for get_api.py
#url=('http://localhost:5000/api/2/4')


url=('http://dummy.restapiexample.com/api/v1/employees')
#Site for demo API
headers = {'Content-type': 'application/json'}







r = requests.get(url, headers=headers)

print(r.status_code)
print(r.json())

