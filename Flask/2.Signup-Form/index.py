#############################
#                            #
#      Step2success.in       #
#        copyright           #
##############################           
#Flask is light weighted framework here we are creating functions same like python just difference is here we are mapping the function 
#with @app route so we are calling the function from web and return the data to web
#pip install flask        

from flask import * 

app = Flask(__name__)


import datetime
name='ankit kothari'



#1st function / by default address(home page)
@app.route('/')
def student():
   return render_template('signup.html',time=datetime.datetime.now(),fullname=name)
   #return Static HTML template store in Templates & pass this dynamic varibale time and name in that



# when user fill the details in signup form and send we are using post method then passing all that varibales in this fntn
@app.route('/result',methods = ['POST'])
def result():

   if request.method == 'POST':

      result = request.form
      print('result',type(result),result)
      for key,values in result.items():
         print(key, ':' , values)

      #db query insert into this ...
      #Insert into user 
      return render_template("result.html",result = result)

      





	

if __name__ == '__main__':
   app.run(port=5088,debug=True)
   #change port acc to your convienence