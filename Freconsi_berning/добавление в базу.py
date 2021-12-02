import pandas as pd
import math

df = pd.read_excel('База_подшипников_Россия.xlsx')

nomer = 999999
d = 3000
D = 6000
la = 10
dw = 99
Z = 666

row = pd.Series({'Номер_подшипника':nomer,'Внутренний_диаметр':d,'Внешний_диаметр':D,'Угол_с_опорой':la,'Диаметр_дел_качения':dw,'Число_тел_качения':Z},name=len(df))

df = df.append(row)

writer = pd.ExcelWriter('База_подшипников_Россия.xlsx')

df.to_excel(writer,index=False)
writer.save()
print('Фаил сохранен в текущую директорию.')


