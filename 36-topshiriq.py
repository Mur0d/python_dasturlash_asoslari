# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:58:32 2022

@author: user
"""

def katta_son(a,b,c):
  return max(a,b,c)  


def title(*matn):
    nat = []
    for n in matn:
        nat.append(n.title())
    return nat

def juft_son(a,b):
    sonlar = range(a,b)
    juft = []
    for n in sonlar:
        if n%2 == 0:
            juft.append(n)
    return juft

def son_fibo(n):
    if (n-2)+(n-1)==n:
        return True
    else:
        return False

        
