# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:38:55 2021

@author: user
"""

def tub_son_yasa(min,max):
    tub_son = []
    for n in range(1,max+1):
        tub=True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2,n):
                if n % x ==0:
                    tub = False
        if tub:            
            tub_son.append(n)
    return tub_son            


tub_son = tub_son_yasa(12,122)
print(tub_son)

def fibonacci(son):
    sonlar = []
    for n in range(son):
        if n == 0 or n == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[n-1]+sonlar[n-2])
    return sonlar


sonlar = fibonacci(27)  
print(sonlar)          
    