import pandas
#import pandas libarary
#pip install pandas on cmd

#reading file in the same folder or provide the path
df=pandas.read_excel("input.xlsx")
# or to provide shhet name
df=pandas.read_excel("input.xlsx", sheet_name='Sheet1')
#or #use this oine if your headingg is not placed in by deafult o position change 0 position
df=pandas.read_excel("input.xlsx",header=0)

#to print columns read in excel
print(df.keys())
#or
print(df.columns)


#print(df)
#print the whole file
#################################################


#print only 1st colum
col_1=df['switch']
col_2=df['input']
print(col_1,col_2)