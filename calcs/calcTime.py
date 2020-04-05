# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 01:41:41 2020

@author: freya
"""

from getValues import getValues

class calcTime():
    
    '''
    Variabels for Modules
    '''
    def __init__(self):
        self.sm1v = 0.2
        self.sm1e = 0.5
        self.sm2v = 0.3
        self.sm2e = 0.6
        self.sm3v = 0.5
        self.sm3e = 0.7
        
        self.em1e = -0.3
        self.em2e = -0.4
        self.em3e = -0.5
        
        self.pm1e = 0.4
        self.pm1v = -0.15
        self.pm1p = 0.04
        self.pm1e = 0.6
        self.pm1v = -0.15
        self.pm1p = 0.06
        self.pm1e = 0.8
        self.pm1v = -0.15
        self.pm1p = 0.10
        
        self.beacon = 0.5
        
        self.assembler1 = 0.5
        self.assembler2 = 0.75
        self.assembler3 = 1.25
        
        self.oilpump = 1
        self.raffinery = 1
        self.chemicalplant = 1
        self.centrifuge = 1
        
        self.furnace1 = 1
        self.furnace2 = 2
        self.efurnace = 2
    
    '''
    TODO
    '''
    def time(self, item):
        db = getValues()
        time = int(db.getTime(item))
        
        return time
    
    # To calculate the Production rate of the builder (assembler, chem plant, usw..)
    def builderPR(self, builder, module1=0, module2=0, module3=0, module4=0):
        pr = builder
        pr = pr + (pr * (module1 + module2 + module3 + module4))
        return pr
    
    '''
    TODO --> To calculate the Power usage of the builder
    '''
    def builderPU():
        pass
    
    '''
    TODO --> To calculate the Productivity of the builder
    '''
    def builderPD():
        pass
    
    '''
    TODO --> To calculate the boost of a beacon
    '''
    def beaconBoost(self, module1, module2):
            
        pass
    
    
    '''
    # Testing Area
    # 
    # TESTING AREA
    # 
    # Testing Area
    '''
    def main(self):
        # print(a.time('advanced-circuit', 'true', self.assembler3))
        print(a.builderPR(self.assembler3, self.sm3v, self.sm3v, self.sm3v, self.sm3v))

if __name__ == "__main__":
    a = calcTime()
    a.main()

       



























    