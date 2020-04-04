#############################
#                            #
#      Step2success.in       #
#        copyright           #
############################## 

from flask import Flask ,render_template,jsonify, request
app = Flask(__name__)
import datetime
import time

# Create a function that will provide current data and time. In HTML side we uses bootstrap .
#Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.
#It contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface component

#IF we want our time updated in html page so we nned to refresh page every seond so we uses HTML auto refresh in HTML file.
#<meta http-equiv="refresh" content="2">

@app.route('/')
def show():
	
	current_time=str(datetime.datetime.now())
	now = datetime.datetime.now()
	time = str(now.hour)+" : "+ str(now.minute)
	print(time)
	return render_template('date.html',current_time=current_time,time=time)


	



if __name__ == '__main__':
    app.run(port= 5038)



    

