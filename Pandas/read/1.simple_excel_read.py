import pandas
#import pandas libarary
#pip install pandas on cmd

#reading file in the same folder or provide the path
df=pandas.read_excel("input.xlsx")
#print the whole file
print(df,type(df))