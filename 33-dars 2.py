# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 20:18:14 2022

@author: user
"""
import pickle
filename = 'pi_million_digits.txt'

with open(filename) as file:
    pi = file.read()
# print(pi)

# def t_sana_qid():
#     sana = input("tug'ilgan sanani kiriting. Misol uchun:(18.06.1997 bo'lsa 18061997): ")
#     if sana in pi:
#         javob = 'bor'
#     else:
#         javob = "yo'q"
#     return javob

pi = pi.rstrip()
pi = pi.replace('\n','')
pas = pi = float(pi)
print(pi)


with open('PiBin','wb') as file:
    pickle.dump(pas,file)
