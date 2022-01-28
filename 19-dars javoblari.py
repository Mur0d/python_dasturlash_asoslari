
"""
Created on Mon Nov 22 21:49:03 2021

@author: user
"""
def t_yil_hisobla(ism,yosh):
    """Tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"{ism.title()} {2021-yosh}-yilda tug'ilgan")
#t_yil_hisobla("anvar",25)    
    
    
def son(son):
    """Sonning kvadrati va kubini chiqaruvchi funksiya"""
    print(f"Sonninng kvadrati: {son**2}ga teng\n"
          f"Sonning kubi:{son**3}ga teng")    
#son(22)

def juft_toq(son):
    """Sonning juft yoki toqligini aniqlovchi funksiya"""
    if son%2==0:
        print(f"Siz kiritgan {son} juft son")
    else:
        print(f"Siz kiritgan {son} toq son")
    
#juft_toq(22)    
    
def katta_son(son_1,son_2):
    """Sonlar orasidan kattasini tanlaydi yoki teng ekanini ko'rsatadi"""
    if son_1>son_2:
        print(son_1)
    elif son_2>son_1:
        print(son_2)
    else:
        print(f"{son_1}={son_2}")
        
#katta_son(22,22)   

def son_daraja(son,daraja):     
    """Sonning darajasini hisoblaydigan dastur"""
    print(f"{son}ning {daraja}-darajasi {son**daraja}ga teng")
    
#son_daraja(12,15)


def son_kvadrati(son):     
    """Sonning darajasini hisoblaydigan dasturcha"""
    print(f"{son}ning kvadrati {son**2}ga teng")
    
#son_kvadrati(22)   
       
def son_boluvchi(son):
    """Sonning 2dan 10gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiradi"""    
    son_1=range(2,11) 
    for x in son_1:
        if son%x==0:
            print(f"{son} {x}ga qoldiqsiz bo'linadi")
    
son_boluvchi(100)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    