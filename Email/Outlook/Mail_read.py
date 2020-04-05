import win32com.client
import time
# Reading files of outllok


		
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts;
#connection with outlook

for account in accounts:

	#for multiple accounts in outlook
	
	inbox = outlook.Folders(account.DeliveryStore.DisplayName)
	print(account.DisplayName)

	
	folders = inbox.Folders



	#change inbox name with other folders name
	messages = folders['Inbox'].Items
	
	#to read sub folder under inbox
	#messages = messages = folders['Inbox'].Folders['Incident Audit'].Items
	length=len(messages)
	print(length)

	for i in range(length,0,-1):
		#reading messages one by one
		try:
			message2=messages[i]
					
			sender = str(message2.Sender)
			
			receiver = str(message2.To)
			cc = message2.Cc
			subject = str(message2.Subject)
					
			body = str(message2.Body)

			

			if True:				
			#if (message2.Unread == True) :
				#if you want to print only unread messages and set back to read status with a flag.
							
				message2.Unread =False
				message2.Categories = 'Yellow Category'
				print('sender:',sender)	
				print('subject:',subject)	
				print('body:',body)
				print('\n\n\n')
				time.sleep(5)
		except Exception as e:
			print('Unable to read message',e)
						
							