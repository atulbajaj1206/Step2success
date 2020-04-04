#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################      
# To call post api

import requests
import json

print('flask')


url=('http://localhost:5001/sum')
headers = {'Content-type': 'application/json'}


data= {
"a":2,
"b":3,

}




r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.status_code)
print (r.json())
