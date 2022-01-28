# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 20:54:10 2021

@author: user
"""

def foydalanuvchilar(ismi , familiyasi ,t_yili ,t_joyi ,email ,telefon=None):
    malumot = {"ismi":ismi,
               "familiyasi":familiyasi,
               "t_yili":t_yili,
               "t_joyi":t_joyi,
               "email":email,
               "telefon":telefon}
    return malumot

print("\nSaytimizdagi foydalanuvchilar ro'yxatini tuzing:")
malumotlar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end="")
    ismi = input("Ism: ")
    familiyasi = input("Familiyasi: ")
    t_yili = int(input("Tug'ilgan yili: "))
    t_joyi = input("Tug'ilgan joyini kiriting: ")
    email = input("Email manzil: ")
    telefon = input("telefon raqam: ")
    malumotlar.append(foydalanuvchilar(ismi, familiyasi, t_yili, t_joyi, email, telefon))
    javob = input("Foydalanuvchilar ro'yhati to'liq kiritildimi ?(ha/yo'q)")
    if javob!="ha":
        break
print("Foydalnuvchilar ro'yxati:")
for malumot in malumotlar:
    if malumot['telefon']:
        telefon = malumot['telefon']
    else:
        telefon = "Noma'lum"
    print(f"Foydalanuvchi {malumot['ismi']} {malumot['familiyasi']}.{malumot['t_yili']}-yilda {malumot['t_joyi']}da tug'ilgan. Yoshi {2021-malumot['t_yili']}da . Email: {malumot['email']}. Raqami: {malumot['telefon']}")    
    
    
    
    
    