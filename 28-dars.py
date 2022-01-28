# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 06:43:31 2021

@author: user
 """
class Talaba:#Class nomi.
    def __init__(self,ism,familiya,tyil):#Class xususiyatlari.
        self.name = ism
        self.surname = familiya
        self.byear = tyil
    def tanishtir(self):
          return f"Ismim {self.name} {self.surname} {self.byear}-yilda tug'ilganman"
    def get_name(self):
        return self.name
    def full_name(self):
        return f"{self.name} {self.surname}"
    def yoshi(self,yil):
        return yil-self.byear
        
        
talaba1 = Talaba("Abdulla","Rahmatullayev",2000)
talaba2 = Talaba("Jonibek","G'aniyev",1999)
talaba3 = Talaba("Abror","Esanov",1998)

print(talaba2.tanishtir())
print('yoshim',talaba2.yoshi(2021))


class User:
    def __init__(self,ism,familiya,tyil,login,email,telraqam):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.login = login
        self.email = email
        self.telraqam = telraqam
    def get_name(self):
        return self.ism
    def get_login(self):
        return self.login
    def get_age(self,yil):
        return yil-self.tyil
    def full_name(self):
        return f"Ismi {self.ism} familiyasi {self.familiya}"
    def full_info(self):
        return f"Ismi {self.ism} familiyasi {self.familiya} {self.tyil} yilda tug'ilgan. Telefon: {self.telraqam}"            


user1 = User("Abror", "Esanov", 1998, "DarkLord", "darklord998@gmail.com", 991039998)
user2 = User("Abdulla", "Rahmatullayev", 2000, "Dalbiy", "dalbiy2000@gmail.com", 999868442)
user2 = User("Jonibek", "Ganiyev", 1999, "Shilta", "shilta1999@gmail.com", 995756639)
print(user2.full_info())    
    
    
    
    
    
    
    
    
    
    
    
    