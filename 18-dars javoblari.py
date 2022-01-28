# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 11:43:01 2021

@author: user
"""

buyurtma = []
print("Qanday mahsulotlar buyurtma qilmoqchisiz:")
n=1
#while True:
#    savol = f"{n}-mahsulotni kiriting:\n>>>"
#    mahsulot = input(savol)
#    buyurtma.append(mahsulot)
#    javob = input("yana mahsulot qo'shasizmi ?(ha|yo'q)")
#    if javob == "ha":
#        n+=1
#        continue
#    elif javob == "yo'q":
#        break
#for mahsulot in buyurtma:
#    print(mahsulot.lower())


e_bozor = {}
#print("Mahsulotlar ro'yxatini kiriting")
ishora = True
#while ishora:
#    mahsulot = input("mahsulot nomini kiriting:")
#    narx = input(f"{mahsulot} narxini kiriting:")
#    e_bozor[mahsulot]=int(narx)
#    javob = input("yana mahsulot qo'shishni istaysizmi ?(ha/yo'q)")
#    if javob != "ha":
#        ishora = False
#for mahsulot,narx in e_bozor.items():
#    print(f"{mahsulot} narxi {narx}so'm")        
        


e_bozor = {}
buyurtma =[]
print("Mahsulotlar ro'yxatini kiriting")
ishora = True
while ishora:
    mahsulot = input("mahsulot nomini kiriting:")
    narx = input(f"{mahsulot} narxini kiriting:")
    b_mahsulot = input("Buyurtmani kiriting:")
    e_bozor[mahsulot]=int(narx)
    buyurtma.append(b_mahsulot)
    javob = input("yana mahsulot qo'shishni istaysizmi ?(ha/yo'q)")
    if javob != "ha":
        ishora = False
for mahsulot in e_bozor.keys():
    if mahsulot in buyurtma:
        print(f"{mahsulot} narxi {e_bozor[mahsulot]}so'm")
    else:
        print(f"{mahsulot} do'konimizda yo'q")
        


















































