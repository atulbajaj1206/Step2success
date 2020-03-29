#import pandas libarary
import pandas
from pandas import ExcelWriter
from pandas import ExcelFile
import os
import datetime
#reading file in the same folder or provide the path
df=pandas.read_excel("chassis.xlsx")
print(df)
df.to_csv('chassis1.csv', mode='a', header=True, index=False)
os.system('chassis1.csv')