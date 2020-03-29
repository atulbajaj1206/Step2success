import pandas as pd
import tkinter as tk
from tkinter import filedialog


cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [32000,35000,37000,45000]
        }

df = pd.DataFrame(cars, columns = ['Brand', 'Price'])

#######################
#Tkinter code GUI##
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

def exportExcel ():
    global df
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel (export_file_path, index = False, header=True)

saveAsButtonExcel = tk.Button(text='Export Excel', command=exportExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButtonExcel)

root.mainloop()