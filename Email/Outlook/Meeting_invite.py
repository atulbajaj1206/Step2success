import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application")


def sendMeeting(self,start_time,duration,subject,reason):

	  appt = outlook.CreateItem(1) # AppointmentItem
	  print(start_time)
	  appt.Start = str(start_time)# yyyy-MM-dd hh:mm
	  appt.Subject = subject
	  appt.Duration = duration # In minutes (60 Minutes)
	  appt.Location = "Orange Business Services Carrier Planned Maintenance for GLAXOSMITHKLINE SERV"
	  appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added
	  appt.Body = "HI ALL,"+'\n\n'+'Please find below the details of the activity to avoid alarms for the required device.'+'\n\n'+reason
	  to=self.file_handling()
	  print(to,type(to))
	  for i in to:
	  	appt.Recipients.Add(i) 
	  appt.Save()
	  appt.Send()


	def sendRecurringMeeting(self):    
	  appt = outlook.CreateItem(1) # AppointmentItem
	  appt.Start = "2018-10-28 10:10" # yyyy-MM-dd hh:mm
	  appt.Subject = "Subject of the meeting"
	  appt.Duration = 60 # In minutes (60 Minutes)
	  appt.Location = "Location Name"
	  appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added

	  appt.Recipients.Add("ankit.kothari@orange.com") # Don't end ; as delimiter

	  # Set Pattern, to recur every day, for the next 5 days
	  pattern = appt.GetRecurrencePattern()
	  pattern.RecurrenceType = 0
	  pattern.Occurrences = "5"

	  appt.Save()
	  appt.Send()