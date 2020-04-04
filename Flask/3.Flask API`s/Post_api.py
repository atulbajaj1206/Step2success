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

from flask import Flask, render_template, request,jsonify
app = Flask(__name__)


@app.route('/')
def page():
	return("Hi, web page")




################################
#send with postman app value of and b and it will return you its sum.

@app.route("/sum",methods = ['POST'])
def sum():
	if request.method == 'POST':
		result = request.get_json()
		a=result['a']
		b=result['b']
		print(result)
		c=int(a)+int(b)
		return jsonify({'Result':c})









if __name__ == '__main__':
   app.run(port=5001)


