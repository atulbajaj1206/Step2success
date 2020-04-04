#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
#Flask is light weighted framework here we are creating functions same like python just difference is here we are mapping the function 
#with @app route so we are calling the function from web and return the data to web
#pip install flask
#From Flask we can also create API


#An API is a set of programming code that enables data transmission between one software product and another.
#It also contains the terms of this data exchange in the same format ie json,xml.


#We can use get/post any method.In get we are transmitting data with url its not secured but bit easy IE: www.googlemaps/?location_id=12020
#in post we are sending with encapsulation
from flask import * 

app = Flask(__name__)




@app.route('/')
def home():
   return ("Welcome")




	
# Get Transmitting data with url

@app.route('/api/<no1>/<no2>', methods = ['GET']) 
def disp1(no1,no2):
	#print(comment)
	no1=int(no1)
	no2=int(no2)
	sum=no1+no2
	product=no1*no2


	## Your Db query here...
	return jsonify({'sum': sum,'And Product is':product,'no1':no1}) 
	




if __name__ == '__main__':
   app.run(port=5000)