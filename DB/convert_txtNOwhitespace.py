# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:00:10 2020

@author: freya
"""

fileToSearch  = 'recipies.txt'

textToSearch = ' @ '
# textToSearch02 = ''
# textToSearch03 = ''

textToReplace = ','
# textToReplace02 = ''
# textToReplace03 = ''

with open(fileToSearch) as a:
    for line in a:
        if textToSearch in line :
            print('Match Found')
            out_file = open("recipies.txt", "w")
            out_file.write(line.replace(textToSearch, textToReplace))
            out_file.close()
        else:
            print('Match Not Found!!')
        
fileToSearch.close()

