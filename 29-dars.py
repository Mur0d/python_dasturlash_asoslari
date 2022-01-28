# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 20:56:50 2021

@author: user
"""
class Avto:
    def __init__(self,konsern,model,rang,korobka,km,yil,narh):
        self.konsern = konsern
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.km = km
        self.yil = yil
        self.narh = narh
    
    def get_avto(self):
        return f"Model: {self.model}. \n Rangi: {self.rang} "
    def get_konsern(self):
        return self.komsern
    def get_model(self):
        return self.model
    def get_rang(self):
        return self.rang
    def get_korobka(self):
        return self.karobka
    def get_yil(self):
        return self.yil
    def get_narh(self):
        return self.narh
    def get_info(self):
        return f"Konsern: {self.konsern}. Model: {self.model}. Rang: {self.rang}. Korobka: {self.korobka}. Km: {self.km} yurgan. Yili: {self.yil}. Narhi: {self.narh}"
    def update_km(self,km):
        self.km = km
    def set_km(self,plus):
        return self.km + plus
    def set_narh(self,narh):
        self.narh = narh


class Avtosalon():
    def __init__(self,nomi,manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.avtolar = []
        self.avto_soni = 0
    def add_avto(self,avto):
        self.avtolar.append(avto)
        self.avto_soni += 1
    def get_nomi(self):
        return self.nomi
    def get_manzili(self):
        return self.manzili
    def get_avtolar(self):
        return [avto.get_info() for avto in self.avtolar]
   
    
    
Urgut_avto = Avtosalon("Urgut avto","Urgut tumani yangi bozori")
avto1 = Avto("GM","malibu",'qora','avtomat',100000,2018,"27000$")
avto2 = Avto("BMW","X6",'qora','avtomat',70000,2016,"90000$")
avto3 = Avto("GM","cobalt",'oq','mexanika',120000,2015,"7000$")
Urgut_avto.add_avto(avto1)
Urgut_avto.add_avto(avto2)
Urgut_avto.add_avto(avto3)
print(Urgut_avto.avto_soni)
u_savdo = Urgut_avto.get_avtolar()



def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]