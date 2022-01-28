# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:15:32 2022

@author: user
"""

import pickle

talaba1 ={'ism':'Abdulla','familiya':'Hasanov','tyil':1988}
talaba2 ={'ism':'Abror','familiya':'Esanov','tyil':1998}

with open('Talaba','wb') as f:
    pickle.dump(talaba1,f)
    pickle.dump(talaba1,f)
