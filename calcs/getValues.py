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
        #Import from GUI
        # dbitems = 'DB/data.json'
        # dbmodule = 'DB/module.json'
        # dbpr = 'DB/prBuilder.json'
        #Local Text Import
        dbitems = '../DB/data.json'
        dbmodule = '../DB/module.json'
        dbpr = '../DB/prBuilder.json'
        
        self.data = json.loads(open(dbitems).read())
        self.module = json.loads(open(dbmodule).read())
        self.pr = json.loads(open(dbpr).read())
    
    
    def getTime(self, item):
        '''
        @param string item
        @return integer time
        '''
        try:
            time = self.data['Items'][item]['time']
            return time
        except KeyError:
            error = "Time does not exist"
            return error
        
    def getAmount(self, item):
        '''
        Returns amount of output
        index uneven --> value
        @param string item
        @return list amount
        '''
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
            error = 'Amount does not exist'
            return error
    
    def getIngredients(self, item):
        '''
        Returns Ingredients for Item
        index uneven --> value
        index even --> name of ingredient
        @param string item
        @return list amount
        '''
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
            error = 'Ingredients does not exist'
            return error
    
    def getAllItemNames(self):
        '''
        Returns all item Names
        @return list item
        '''
        list = []
        for i in self.data['Items']:
            list.append(i)
        return list
    
    def getModuleNames(self):
        '''
        Returns all Module Names
        @return list item
        '''
        list = []
        for i in self.module['modules']:
            list.append(i)
        return list
    
    def getBuilderNames(self):
        '''
        Returns all Builder Names
        @return list item
        '''
        list = []
        for i in self.pr['builders']:
            list.append(i)
        return list
    
    def getBeltNames(self):
        '''
        @return string attribute
        '''
        list = []
        for i in self.pr['belts']:
            list.append(i)
        return list
    
    def getModuleAttributs(self, module, attribute):
        '''
        @param string attribut (speed, energy, productivity)
        @return string attribute
        '''
        try:
            value = self.module['modules'][module][attribute]
            return value
        except KeyError:
            error = "Module or Attribute does not exist"
            return error
        
    
    def getBuilderPr(self, builder):
        '''
        @param string buildername
        @return string pr
        '''
        try:
            value = self.pr['builders'][builder]['pr']
            return value
        except KeyError:
            error = "Builder does not exist"
            return error
        
    def getBeltSpeed(self, belt):
        '''
        @param string Belt
        @return string pr
        '''
        try:
            value = self.pr['belts'][belt]['speed']
            return value
        except KeyError:
            error = "Belt does not exist"
            return error
    