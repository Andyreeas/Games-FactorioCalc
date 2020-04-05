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
        
        self.pm1v = -0.15
        self.pm1e = 0.4
        self.pm1p = 0.04
        self.pm1v = -0.15
        self.pm1e = 0.6
        self.pm1p = 0.06
        self.pm1v = -0.15
        self.pm1e = 0.8
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


    def time(self, item, builder, module1 = 0, module2 = 0, module3 = 0, module4 = 0, number = 0, beamodule1 = 0, beamodule2 = 0):
        '''
        To calculate Time of item with boost
        '''
        calc = calcTime()
        db = getValues()
        time = int(db.getTime(item))
        pr = calc.builderPR(builder, module1, module2, module3, module4)
        boost = calc.beaconBoostPR(number, beamodule1, beamodule2)
        time = time / (pr * boost)
        
        return time
    
    def builderPR(self, builder, module1=0, module2=0, module3=0, module4=0):
        '''
        To calculate the Production rate of the builder
        @param builder (assembler, chem plant, usw..)
        @param modules 1 - 4 (Optional)
        return float pr
        '''
        pr = builder
        pr = pr + (pr * (module1 + module2 + module3 + module4))
        return pr
    
    def beaconBoostPR(self, number, module1=0, module2=0):
        '''
        To calculate the boost of beacon's
        return float pr%
        '''
        i = 0
        boost = 0
        while i < number:
            boost = boost + module1 + module2
            i = i + 1
        return boost
    
    def power():
        '''
        TODO --> To calculate the Power usage
        '''
        pass
    
    def builderPU():
        '''
        TODO --> To calculate the Power usage of the builder
        '''
        pass
    
    def beaconBoostPU():
        '''
        TODO --> To calculate the Power usage with Beacon's
        '''
        pass
    
    def builderPD():
        '''
        TODO --> To calculate the Productivity of the builder
        '''
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
        # pr = a.builderPR(self.assembler3, self.sm3v, self.sm3v, self.sm3v, self.sm3v)
        time = a.time('accumulator', self.assembler3, self.sm3v, self.sm3v, self.sm3v, self.sm3v, 4,self.sm3v, self.sm3v)
        return time

if __name__ == "__main__":
    a = calcTime()
    print(a.main())

       