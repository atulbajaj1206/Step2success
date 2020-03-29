
import pandas as pd
from pandas import ExcelWriter
#importing function to write excel

from pandas import ExcelFile
#operating system importing for opeing file at end
import os
import datetime

file_name='s2s.csv'
c=1





def logs(col_a,col_b,col_c):
		print('logging')

		#preparing data frame(key in index and value will be appended in colmuns)
		

		dict = {'Oceane Ticket no.':col_a,  'Remedy Ticket no': col_b,'Create Date':col_c }

		
		df = pd.DataFrame(dict, index=[c])

		if c==1:
			#counter if this is first time file is create then create header else skip header,mode=a -append mode,index- serial no wil be written on excel
				df.to_csv(file_name,mode='a',header=True,index=False)
		else:
			df.to_csv(file_name,mode='a',header=False,index=False)



#calling csv write funtion 100 times with 100 diff values

for i in range(0,20):
	
	logs(i,i,datetime.datetime.now())
	#increasing counter so that header will be skipped
	c+=1
		
		
		
os.system(file_name)

		


