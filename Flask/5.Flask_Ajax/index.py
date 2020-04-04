#############################
#                            #
#      Step2success.in       #
#        copyright           #
############################## 



# in last eg we are refresing page to get new content but it will cause to load whole page css and js and cause delay.
# in order to get it real time we are using AJAX.
#AJAX stands for Asynchronous JavaScript and XML. AJAX is a new technique for creating better, faster, and more interactive web applications
#With AJAX, when you hit submit, JavaScript will make a request to the server, interpret the results, and update the current screen. 
#In the purest sense, the user would never know that anything was even transmitted to the server.

# In AJAX only a part of data is transmiited and change in web page not whole page.
# Only Jquery has capability o change the HTML in run time

# With AJAX you can create real time form validation.
from flask import Flask ,render_template,jsonify, request
app = Flask(__name__)
import datetime
import time



@app.route('/')
def show():
	
	current_time=str(datetime.datetime.now())
	now = datetime.datetime.now()
	time = str(now.hour)+" : "+ str(now.minute)
	print(time)
	return render_template('date.html')



#after the main page loaded.Api is calling frequently by javascript and this api will transmitting only the data we weant to change in JSON.
@app.route('/api')
def show_all():
	
	current_time=str(datetime.datetime.now())
	now = datetime.datetime.now()
	time = str(now.hour)+" : "+ str(now.minute)
	return jsonify({'current_time':current_time,'time':time})
	



if __name__ == '__main__':
    app.run(port= 5035)



    

