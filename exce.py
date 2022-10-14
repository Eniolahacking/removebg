import pandas as pd
import os
fileo=r'/storage/emulated/0/Donwload/Data Bleanding File Two.xlsx'
you=pandas.read_excel(fileo)
print(you)
print(you.loc[[1,6],["BONUS"]])
os.startfile(r'/storage/emulated/0/Donwload/Data Bleanding File Two.xlsx')
