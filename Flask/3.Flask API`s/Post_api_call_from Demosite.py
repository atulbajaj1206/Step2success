#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################      
# To call post api

import requests
import json




url=('http://dummy.restapiexample.com/api/v1/create')
headers = {'Content-type': 'application/json'}


data= {"name":"test","salary":"123","age":"23"}
print(json.dumps(data))



r = requests.post(url, data=json.dumps(data), headers=headers)
print(r)

print(r.status_code)
print (r.json())
