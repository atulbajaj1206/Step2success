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