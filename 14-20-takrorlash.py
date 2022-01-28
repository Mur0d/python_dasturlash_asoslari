# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 08:32:26 2021

@author: user
"""

# otam = {"ismi":'shavkat','familiyasi':'narzullayev','tugilgan yili':1950,'tug\'ilgan joyi':'Gijduvon tumani'}
# print(f"Otam {otam['ismi']} {otam['familiyasi']} {otam['tugilgan yili']}-yilda tug'ilgan")

# sev_taom = {}
# sev_taom['ali']='osh'
# sev_taom['vali']='manti'
# sev_taom['joni']='somsa'
# for k,v in sev_taom.items():
#     print(f"{k.title()}ning sevimli taomi {v}")
    
# python = {"fload":"kasr son","int":"butun son","str":"matn","key":"kalit so'z","value":"qiymat","if":"agar","for":"uchun","or":"yoki","and":"va"}    
# keyword = input("Kalit so'znikiriting: ")
# if keyword == '':
#       qiymat = input("Qiymatni kiriting: ")
#       python_1 = {}
#       for key,value in python.items():
#           python_1[value] = key
#       print(f"{python_1[qiymat]}")         
# else:
#     print(f"{python[keyword]}")         



         

# python = {"fload":"kasr son","int":"butun son",
#           "str":"matn","key":"kalit so'z","value":"qiymat",
#           "if":"agar","for":"uchun","or":"yoki","and":"va"} 

# for key,value in sorted(python.items()):
#     print(f"Kalit : {key.title()}\n Qiymat: {value.title()}")
 

   

# davlatlar = {'Rossiya':'Moskva','Uzbekistan':'Toshkent','Qirgiziston':'Bishkek',
#              'Qozogiston':'Nursuton','Malaziya':'Kuala-lumpur','Italiya':'Rim',
#              'Singapur':'Singapur','AQSH':'Washington'}
# print("Dunyo davlatlari:            Davlatlar poytaxtlari:  ")
# for key,value in sorted(davlatlar.items()):
#     print(f"{key}""                   "f"{value}")




# adiblar = {"Alisher navoiy":['xamsa','lison ut-tayr','hayrat ul-abror'],
#            "Erkin Vohidov":['bahor nafasi','boychechagim',"she'lar"],
#            "Anvar Narzullayev":['pythonda dasturlash asoslari', 'django','c++']}
# for key,value in adiblar.items():
#     print(f"{key}ning asarlari:")
#     for asar in value:
#         print(f"{asar.title()}")
        



# sev_kinolar = {'ali':[],'vali':[],"g'ani":[],'joni':[]}
# for ism,kinolar in sev_kinolar.items():
#     for n in range(3):
#         kinolar.append(input(f"{ism.title()}ning {n+1}-sevimli filmini kiriting: "))        
# for ism,kinolar in sev_kinolar.items():
#     print(f"{ism.tile()}ning sevimli filmlari:")        
#     for kino in kinolar:
#         print(f"{kino}")
          
        
# savol = "yoqtirgan kitobingizni kiriting "
# savol +="\n(tsiklni toxtatish uchun 'stop' yozing):>>>"
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(f"Foydalanuvchining sevimli kitobi: \n{qiymat.title()}")


# savol = "Muzeyga xush kelibsiz. Yoshingiz nechida."
# savol += "\n(kiruvchilar qolmaganda 'stop' yozing):>>>"
# while True:
#     yosh = input(savol)
#     if yosh == 'stop':
#         break
#     else:     
#         if int(yosh)<=7:
#             print("sizga kirish 2000 so'm")
#         if 7<int(yosh)<=18:
#             print("Sizga kirish 5000 so'm")
#         if 18<int(yosh)<65:
#             print("Sizga kirish 10000 so'm")
#         if int(yosh)>=65:
#             # print("sizga tekin. Kirishingiz mumkin.")
    

# savol = 'Buyurtmangizni kiriting'
# savol += "\n(boshqa buyurtmangiz qolmasa 'exit' yozing)"
# buyurtma = []
# while True:
#     buyum = input(savol)
#     if buyum == 'exit':
#         break
#     else:
#         buyurtma.append(buyum)
# print("Buyurtmangiz ro'yxati:")        
# for buyum in buyurtma:
#     print(f"{buyum.title()}")        

# e_bozor = {}
# while True:
#     buyum = input("Buyumni kiriting:")
#     narh = int(input("narxni kiriting:"))
#     javob = input("Yana mahsulot kiritasizmi ?(ha/yo'q)")
#     if javob== "yo'q":
#         break
#     else:
#         e_bozor[buyum] = narh
# print("bozordagi mahsulotlar va ularning narhlari:")        
# for key,value in e_bozor.items():
#     print(f"{key.titile()} narhi: {value}so'm")



# def yosh_hisobla(ism,yosh):
#     """Yosh hisoblaydigan funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n",
#           f"Tug'ilgan yili: {2021-yosh}-yil")

# yosh_hisobla("abdulla",21)


# def hisobla(x):
#     """Kvadrat va kubni hisoblaydigan funksiya"""
#     print(f"Son kvadrati: {x**2}\n",
#           f"Son kubi: {x**3}")

# hisobla(21345)


# def qoldiqsiz(son):
#     for n in range(2,11):
#         if son%n == 0:
#             print(f"{son} {n}ga qoldiqsiz bo'linadi.")
            
# qoldiqsiz(100) 

# def foydalanuvchilar_royxati(ism,familya,t_yil,t_joy,email,telefon=None):
#     foydalanuvchi = {'ism':ism,
#                      'familiya':familiya,
#                      't_yil':t_yil,
#                      't_joy':t_joy,
#                      'email':email,
#                      'telefon':telefon,
#                      'yosh':2021-t_yil}
#     return foydalanuvchi
# print("Foydalanuvchilar ro'yxatini kiriting:")
# foydalanuvchilar = []
# while True:
#     ism = input("Ismni kiriting: ")    
#     familiya = input("Familyani kiriting: ")
#     t_yil =int(input("tug'ilgan yilni kiriting: "))
#     t_joy = input("Yashash manzilini kiriting: ")
#     email = input("email manzil: ")       
#     telefon = input("telefon raqam: ")
#     javob = input("protsesni yakunlashni istaysizmi ? (ha/yo'q)")
#     foydalanuvchilar.append(foydalanuvchilar_royxati(ism,familiya,t_yil,t_joy,email,telefon))
#     if javob == 'ha':
#         break
# for foydalanuvchi in foydalanuvchilar:
#     print(f"foydalanuvchi {foydalanuvchi['ism'].title()} {foydalanuvchi['familiya'].title()}",
#           f"{foydalanuvchi['t_yil']}-yilda tug'ilgan. Yashash manzili: {foydalanuvchi['t_joy']}",
#           f"pochtasi: {foydalanuvchi['email']}.Telefoni:{foydalanuvchi['telefon']} ")    


# def maximum(a,b,c):
#     maks = [a,b,c]
#     print(max(maks))
#     return maks
# maks_1 = maximum(1,2,3)
# print(maks_1)

# while True:
#         son = input("sonni kirit: ")
#         if son == "stop":
#             break
#         elif int(son)<0:
#             continue
#         else:
#             print(float(son)**(1/2))

# def tub_son_top(min,max):
#     tub_son = []
#     for n in range(min,max+1):
#         tub = True
#         if n==1:
#             tub = False
#         elif n==2:
#             tub =True
#         else:
#             for x in range(2,n):
#                 if n % x == 0:
#                     tub = False
#         if tub:            
#             tub_son.append(n) 
#     return tub_son

# tub_son_1 = tub_son_top(22,122)
# print(tub_son_1)



# def fibonacci(son):
#     sonlar = []
#     for n in range(son):
#         if n == 1 or n == 0:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[n-2]+sonlar[n-1])
#     return sonlar

# sonlar1 = fibonacci(22)        
# print(sonlar1)












