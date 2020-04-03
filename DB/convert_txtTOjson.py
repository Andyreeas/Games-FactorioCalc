# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:29:01 2020

@author: freya
"""

import json 
  
# the file to be converted 
file = 'recipiesConverted.txt'

dict01 = {}
dict02 = {} 
dict03 = {} 
dict04 = {}

fields =['item', 'time', 'amount', 'Ingredients'] 
  
with open(file) as f:
    for line in f:
        # loop for one line (reset)
        i = 0
        # reading line by line from the text file 
        # separator , / max 12 splits --> fields
        temp = list(line.strip().split(',', 50))
        # reset dict02
        dict02 = {}
        # -------------------------------
        # Item, time into Dictionary02
        while i < 2: 
            dict02[fields[i]]= temp[i]
            i = i + 1
        # -------------------------------
        # Amount new Dictionary04
        dict04 = {}
        while i < temp.index(fields[3]):
            if i+1 == temp.index(fields[3]):
                dict04[fields[2]] = temp[i]
            else:
                dict04[temp[i+1]] = temp[i]
            i = i + 2
        dict02[fields[2]] = dict04
        # -------------------------------
        # Ingredients new Dictionary03 into 02
        dict03 = {}
        while i < len(temp):
            if temp[i] == 'Ingredients':
                i = i + 1
            dict03[temp[i+1]] = temp[i]
            i = i + 2
        dict02[fields[3]] = dict03
        # -------------------------------
        # Create Json Object with item Name
        na = dict02['item']
        # Enter Json Object with item Name
        dict01[na]= dict02
        
# Write Dictionary into Json
out_file = open("data.json", "w")
json.dump(dict01, out_file)
out_file.close()