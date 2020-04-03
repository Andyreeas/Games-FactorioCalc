# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:29:01 2020

@author: freya
"""

import json 
  
  
# the file to be converted 
file = 'recipies.txt'

out_file = open("data.json", "w") 
out_file.close()

dict02 = {} 
dict01 = {} 
  
fields =['item', 'time', 'produces', 'ingredients'] 
  
with open(file) as f:
    for line in f:
        # loop for one line (reset)
        i = 0
        # reading line by line from the text file 
        # separator ,
        temp = list( line.strip().split('@'))
        # reset dict02
        dict02 = {}
        while i < len(fields): 
            # creating dictionary for each employee 
            dict02[fields[i]]= temp[i] 
            i = i + 1
        na = dict02['item']
        dict01[na]= dict02
        out_file = open("data.json", "w")
        json.dump(dict01, out_file)
        out_file.close()