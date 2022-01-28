# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#a = {'ism':'Alisher Navoiy','t_yil':1441,'t_joy':"Hirot"}   
#b = {'ism':'Abdulla Qodiriy','t_yil':1898,'t_joy':'Farg\'ona'}
#c = {'ism':'Erkin Vohidov','t_yil':1936,'t_joy':'Toshkent'}
#adiblar = [a,b,c]
#for adib in adiblar:
#    print(f"{adib['ism']} {adib['t_yil']}-yilda {adib['t_joy']}da tug'ilgan")
    

    


#adiblar = {
#          'Abu Abdulloh Muhammad ibn Ismoil' : ["Al-jome' as-sahih",'Al-adab al-mufrad','At-tarix al-kabir'],
#          'Abdulla Qodiriy' : ["O'tkan kunlar",'Mehrobdan chayon','Obid ketmon'],
#          'Erkin Vohidov': ['Tong nafasi','O\'zbegim','Qiziquvchan Matmusa'],
#          'Alisher Navoiy' : ['Xamsa','Lison ut-Tayr','Mahbub ul-Qulub']
#          }
#for adib, asarlar in adiblar.items():
#    print(f"\n{adib.title()} ning mashxur asarlari:")
#    for asar in asarlar:
#        print(asar)
              
   
    
   
    
   

#print("Do'stlaringizni sevimli kinolarini kiriting:")
#dost = ['Ali', 'Vali', 'Joni']
#x = []
#y = []
#z = []
#for m in dost[:3]:
#    print(f"{m}ning sevimli kinolari:" ,end = '')
#    for n in  range(3):
#        kino = (input(f"{n+1}-kinoni kiriting:\n"))
#        if m == "Ali":
#            x.append(kino)
#        if m == "Vali":
#            y.append(kino)
#        if m == "Joni":
#            z.append(kino)
#
#dostlar = {"ali" : x, 'vali' : y, 'joni' : z}
#for ism,filmlar in dostlar.items():
#    print(f"\n{ism.title()}ning sevimli filmlarini:")
#    for film in filmlar:
#       print(f'{film}')



    

dostlar = {"Ali":[],"Vali":[],"Joni":[]}

#for k,v in dostlar.items():
  #  for n in range(3):
#        v.append(input(f"{k}ning {n+1}-filmini kiriting: "))
#for ism,kinolar in dostlar.items():
#    print(f"{ism}ning sevimli filmlari")
#    for kino in kinolar:
#        print(kino.upper())




davlatlar = {
            "o'zbekiston" : {'poytaxt':'toshkent',
                             'hudud': 448978,
                             'aholi': 35000000,
                             'pul birligi': "so'm"},
            
             "rossiya" : {'poytaxt':'moskva',
                             'hudud': 17098246,
                             'aholi': 144000000,
                             'pul birligi': "rubl"},
             
             "aqsh" : {'poytaxt':'vashington',
                             'hudud': 9261418,
                             'aholi': 327000000,
                             'pul birligi': "dollar"},
             
             "malayziya" : {'poytaxt':'kuala-lumpur',
                             'hudud': 329750,
                             'aholi': 250000000,
                             'pul birligi': "rinngit"}
             }
#for ism,info in davlatlar.items():
#    if ism in davlatlar.keys():
#        print(f"{ism.title()}ning poytaxti {info['poytaxt']} shahri.\n"
#              f"Hududi:{info['hudud']}.\n"
#              f"Aholisi:{info['aholi']}.\n"
#           f"Pul birligi:{info['pul birligi']}.\n")
        
        
davlat = {"o'zbekiston" : {'poytaxt':'toshkent',
                             'hudud': 448978,
                             'aholi': 35000000,
                             'pul birligi': "so'm"},}
joy = input("Davlat nomini kiriting: ")
for hudud,info in davlat.items():
    if joy in hudud:
         print(f"Hududi:{info['hudud']}.\n"
              f"Aholisi:{info['aholi']}.\n"
              f"Pul birligi:{info['pul birligi']}.\n")
    else:
        print("Bu davlat haqida ma'lumotimiz yo'q!")
         


              
    
        
















