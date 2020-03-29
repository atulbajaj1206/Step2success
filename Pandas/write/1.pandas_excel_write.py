import pandas as pd
import os




#creating data frame key-header,value column details

cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [32000,35000,37000,45000],
        'color':['Red','Blue','White','yellow'],

        }

df = pd.DataFrame(cars, columns = ['Brand', 'Price','color'])
print(df)

df.to_excel (r'export_dataframe.xlsx', index = False, header=True)

os.system('export_dataframe.xlsx')


