# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:48:14 2020

@author: freya
"""


import json

class calcs():
    
    def __init__(self):
        database = "../DB/data.json"
        self.data = json.loads(open(database).read())

    def readJson(self):
        print(self.data)

    def get_time(self, item):
        try:
            print(self.data['Items'][item]["time"])
        except KeyError:
            print("Item doesn't exist")
    
    def get_amount(self, item):
        try:
            print(self.data['Items'][item]["amount"])
        except KeyError:
            print("Item doesn't exist")
    
    def get_allItemNames(self):
        for i in self.data['Items']:
            print(i)
            
calc = calcs()
#calc.readJson()
#calc.get_time('uranium-processing')
#calc.get_amount('uranium-processing')
#calc.get_allItemNames()