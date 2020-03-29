"""The first step is to create an SMTP object, each object is used for connection 
with one server."""
print('start')
import smtplib
server = smtplib.SMTP('smtp exchnage name', port)

#Next, log in to the server
server.login("login", "passowrd")
server.starttls()
server.ehlo_or_helo_if_needed()
#Send the mail
msg='Subject:Demo.This is a demo ,body:ankit'
print('start2')
server.sendmail('gsk.dcsc.delhi@orange.com','ankit.kothari@orange.com', msg)


print('done')

################     working      ######################################