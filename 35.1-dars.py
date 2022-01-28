# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 16:45:26 2022

@author: user
"""

# yosh = input("Yoshingizni kiriting: ")

# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiriting. Iltimos !!!")
# else:
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz.")


# ZeroDivisionError

# x,y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("O ga bo'lib bo'lmaydi.")


# IndexError  
# mevalar = ['anor','olma','olcha','uzum']
# try:
#     print(mevalar[5])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor")

# KeyError

# user = {'username':'Murodbek',
#         'status':'user',
#         'email':'murodbek223@gmil.com',
#         'phone':"998 33 007 10 71"
#         }
# key = 'email'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas")
    
    

filename ='masha.txt'
try:
    with open(filename) as f:
        text = f.load()
except FileNotFoundError:
    print(f'{filename} mavjud emas')


















