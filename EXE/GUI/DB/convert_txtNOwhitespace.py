# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:00:10 2020

@author: freya
"""

fileToSearch  = 'recipies.txt'
i = 0

with open(fileToSearch) as a:
    for line in a:
        temp = list(line.strip().split('@'))
        
        text = line.replace(' ','')
        text = text.replace('@',',')
        text = text.replace('seconds','')
        text = text.replace('Produces:','')
        
        na = str(':' + temp[0])
        na = na.replace(' ','')
            
        text = text.replace(na,'')
        text = text.replace(',,',',')
        text = text.replace(':',',')
        text = text[:-2]
        text = text + '\n'

        out_file = open('recipiesConverted.txt', 'a+')
        out_file.write(text)
        out_file.close()
