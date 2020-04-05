#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################      
# To call post api
# site https://reqres.in/

import requests
import json




url=('https://reqres.in/api/users')
headers = {'Content-type': 'application/json'}


data= {"name":"test","job":"123"}
print(json.dumps(data))



r = requests.post(url, data=json.dumps(data), headers=headers)

print(r.status_code)
print (r.json())
