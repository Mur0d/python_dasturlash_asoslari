# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 05:28:47 2021

@author: user
"""


savol ="Yoqtirgan kitobingizni kiring: "
savol += "(dasturni to'xtatish uchun 'stop' buyrug'inikiting)\n"  
qiymat = ''
#while qiymat != 'stop':
#    qiymat = input(savol)
#    if qiymat != 'stop':
#        print(qiymat)


savol = "Yoshingiz nechida"
savol += "(Muzeyga kiruvchilar tugaganda 'stop' deb yozing)\n>>>>"    
#puma = True
#while puma:
  #  yosh = input(savol)
   # if yosh =='stop':
  #      puma = False
  #  else:
   #     if int(yosh)<7:
    #        print("Chipta uchun 2000 so'm to'lang")
   #     if 7<int(yosh)<18:
    #        print("Chiptangiz narxi 3000 so'm")
   #     if 18<int(yosh)<65:
    #        print("Chipta uchun 10000 so'm to'laysiz")
   #     if int(yosh)>65:
    #        print("Sizga tekin. Kirishingiz mumkin")                
    
savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol +="Musbat son kiriting"
savol +="(dasturni to'xtatish uchun 'exit' deb yozing):"
#while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**0.5
#         print(f"{qiymat}ning ildizi {ildiz}gsa teng")
#print("Dastur yakunlandi!!!!!") 
 
savol = "Yoshingiz nechida"
savol += "(Muzeyga kiruvchilar tugaganda 'stop' deb yozing)\n>>>>"  
while True:
    chipta = input(savol)
    if chipta == 'stop':
        break
    else:
        if int(chipta)<7:
             print("Chipta uchun 2000 so'm to'lang")
        if 7<int(chipta)<18:
            print("Chiptangiz narxi 3000 so'm")
        if 18<int(chipta)<65:
           print("Chipta uchun 10000 so'm to'laysiz")
        if int(chipta)>65:
            print("Sizga tekin. Kirishingiz mumkin") 
print("Kechirasiz chiptalar qolmadi")