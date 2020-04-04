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
        return self.data

    def get_time(self, item):
        try:
            time = self.data['Items'][item]["time"]
            return time
        except KeyError:
            error = "Item doesn't exist"
            return error
    
    def get_amount(self, item):
        try:
            amount = self.data['Items'][item]["amount"]
            return amount
        except KeyError:
            error = "Item doesn't exist"
            return error
    
    def get_allItemNames(self):
        list = []
        for i in self.data['Items']:
            list.append(i)
        return list
            
calc = calcs()
#print(calc.readJson())
#print(calc.get_time('uranium-processing'))
#calc.get_amount('uranium-processing')
#print(calc.get_allItemNames())