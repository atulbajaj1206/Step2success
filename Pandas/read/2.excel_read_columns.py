import pandas
#import pandas libarary
#pip install pandas on cmd

#reading file in the same folder or provide the path
df=pandas.read_excel("input.xlsx")


#use this oine if your headingg is not placed in by deafult o position
'''df=pandas.read_excel("input.xlsx",header=1)'''
#print the whole file
#print only 1st colum
col_1=df['switch']
col_2=df['input']
print(col_1,col_2)