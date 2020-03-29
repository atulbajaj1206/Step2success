import pandas
#import pandas libarary
#pip install pandas on cmd

#reading file in the same folder or provide the path
df=pandas.read_excel("input.xlsx")
df_filter=df.filter(['switch',"input", "output"]) 

print(df_filter)
print('======')









