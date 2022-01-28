# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:18:13 2022

@author: user
"""
import json
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data)



# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
# talaba = json.loads(talaba_json)

# with open('data.json','w') as f:
#     json.dump(data,f)
    
# with open('talaba.json','w') as f:
#     json.dump(talaba,f)

# with open('talaba.json') as f:
#     d = json.load(f)
# print(d)


with open('students.json') as f:
    ta = json.load(f)
print(ta)


with open('api-result.json') as f:
    api = json.load(f)
print(api)





