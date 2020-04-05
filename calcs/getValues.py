# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:48:14 2020

@author: freya
@version: 2.0


"""

import json

class getValues():
    
    '''
    Constructor opens Json DB
    '''
    def __init__(self):
        database = '../DB/data.json'
        self.data = json.loads(open(database).read())
    
    '''
    Outputs whole Json
    '''
    def readJson(self):
        return self.data
    
    '''
    @param string item
    @return integer time
    '''
    def getTime(self, item):
        try:
            time = self.data['Items'][item]['time']
            return time
        except KeyError:
            error = "Item doesn't exist"
            return error
        
    '''
    Returns amount of output
    index uneven --> value
    @param string item
    @return list amount
    '''
    def getAmount(self, item):
        dict = {}
        try:
            for i in self.data['Items'][item]['amount']:
                dict[i] = self.data['Items'][item]['amount'][i]
            list = []
            for i in dict:
                list.append(i)
                list.append(dict[i])
            return list
        except KeyError:
            error = 'Item does not exist'
            return error
    
    '''
    Returns Ingredients for Item
    index uneven --> value
    index even --> name of ingredient
    @param string item
    @return list amount
    '''
    def getIngredients(self, item):
        dict = {}
        try:
            for i in self.data['Items'][item]['Ingredients']:
                dict[i] = self.data['Items'][item]['Ingredients'][i]
            list = []
            for i in dict:
                list.append(i)
                list.append(dict[i])
            return list
        except KeyError:
            error = 'Item does not exist'
            return error
    
    '''
    Returns all item Names
    @param string item
    @return list item
    '''
    def getAllItemNames(self):
        list = []
        for i in self.data['Items']:
            list.append(i)
        return list
    