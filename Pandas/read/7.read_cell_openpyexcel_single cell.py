import pandas as pd
import time
import os
import openpyxl

#another library for excel which work on cell basis not like pandas whole sheet basis
file_name='input.xlsx'



	
workbook_obj = openpyxl.load_workbook(file_name)
   
sheet_obj = workbook_obj['Sheet1']


## change your row and col no
    
read_data=(sheet_obj.cell(row=2, column=1).value)
print(read_data)
print('------------------')
