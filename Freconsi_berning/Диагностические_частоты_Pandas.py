import pandas as pd
import math

sales = pd.read_excel('База_подшипников_Россия.xlsx')

nomer = '316'

data = sales[sales['Номер_подшипника'] == nomer]

d = data['Внутренний_диаметр'].values[0]
D = data['Внешний_диаметр'].values[0]
la = data['Угол_с_опорой'].values[0]
dw = data['Диаметр_дел_качения'].values[0]
Z = data['Число_тел_качения'].values[0]

Fr = 1  # Частота в герцах



class PodsipnikFrequency():
    def __init__(self, d = 0, D = 0, dw = 0, Z = 0,la = 0, Fr = 1):
        self.d = d
        self.D = D
        self.dw = dw
        self.Z = Z
        self.la = la
        self.Fr = Fr
        self.Dc = 1/2 * (self.D + self.d)
        
    def Fn(self):
        self.fn = 1/2 * self.Fr * (1 - self.dw / self.Dc* math.cos(self.la * math.pi/180))*self.Z
        return self.fn
    
    def Fvnutr(self):
        self.fvn = 1/2 * self.Fr * (1 + self.dw/self.Dc* math.cos(self.la*math.pi/180))*self.Z
        return self.fvn
    
    def Ftk(self):
        self.ftk = 1/2 * self.Fr * self.Dc/self.dw * (1 - (self.dw**2/self.Dc**2)* math.cos(self.la*math.pi/180)**2)
        return self.ftk
    
    def Fsep(self):
        self.fsep = 1/2 * self.Fr * (1 - self.dw/self.Dc * math.cos(self.la*math.pi/180))
        return self.fsep
    
    def Frequency(self):
        return self.fn, self.fvn, self.ftk, self.fsep

my = PodsipnikFrequency(d , D, dw , Z , la, Fr)

print(nomer ,' - номер подшипника')
print(d, ' - Диматр внутренней обоймы')
print(D, ' - Диматр внешней обоймы')
print(dw, ' - Диматр тел качения')
print(Z, ' - Кол-во тел качения')
print(la, ' - Угол в град')

print()
        
print(my.Fn(),' - перекатывание по наружнему кольцу')
print(my.Fvnutr(),' - перекатывание по внутреннему кольцу')
print(my.Ftk(), ' - вращение тел качения')
print(my.Fsep(),' - сепараторная частотая')