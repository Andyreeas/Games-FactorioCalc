# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 01:41:41 2020

@author: freya
"""

'''RelativeImport for GUI'''
from .getValues import getValues 
'''Import for local test'''
# from getValues import getValues

class calcPR():
    
    '''
    Variabels for Modules
    '''
    def __init__(self):
        # Connection to DataBase
        self.db = getValues()

    def builderAmount(self, itemsneededperMinute, item, builder, module1, module2, module3, module4, beaModule, amountBea):
        '''
        returns Amount of Builders needed to produce itemsneededperMinute
        '''
        ips = self.itemsPerSecond(item, builder, module1, module2, module3, module4, beaModule, amountBea)
        amountBuilder = itemsneededperMinute / (ips * 60)
        return amountBuilder
    
    def builderFullBelt(self, belt, item, builder, module1, module2, module3, module4, beaModule, amountBea):
        '''
        returns Amount of Builders needed to fill specific Belt
        param int belt
        '''
        ips = self.itemsPerSecond(item, builder, module1, module2, module3, module4, beaModule, amountBea)
        belt = db.getBeltSpeed(belt)
        amountBuilder = belt / ips
        return amountBuilder
    
    def itemsPerSecond(self, item, builder, module1, module2, module3, module4, beaModule, amountBea):
        time = self.time(item, builder, module1, module2, module3, module4, beaModule, amountBea)
        amount = self.db.getAmount(item)
        ips = float(amount[1]) / time
        ips *= self.moduleProductivityBoost(module1, module2, module3, module4)
        return ips

    def time(self, item, builder, module1, module2, module3, module4, beaModule, amountBea):
        '''
        To calculate Time of item with boost
        '''
        time = float(self.db.getTime(item))
        pr = self.builderPr(builder, module1, module2, module3, module4, beaModule, amountBea)
        time /= pr
        return time
    
    def builderPr(self, builder, module1, module2, module3, module4, beaModule, amountBea):
        '''
        To calculate the Production rate of the builder
        @param builder (assembler, chem plant, usw..)
        @param modules 1 - 4 
        return float pr
        '''
        builderpr = db.getBuilderPr(builder)
        builderpr += (builderpr * self.moduleSpeedBoost(module1, module2, module3, module4))
        builderpr += (db.getBuilderPr(builder) * self.beaconBoostPR(amountBea, beaModule))
        return builderpr
    
    def moduleSpeedBoost(self, module1=0, module2=0, module3=0, module4=0):
        speedBoost = db.getModuleAttribut(module1, 'speed')
        speedBoost += db.getModuleAttribut(module2, 'speed')
        speedBoost += db.getModuleAttribut(module3, 'speed')
        speedBoost += db.getModuleAttribut(module4, 'speed')
        return speedBoost
    
    def moduleProductivityBoost(self, module1, module2, module3, module4):
        prodBoost = db.getModuleAttribut(module1, 'productivity')
        prodBoost += db.getModuleAttribut(module2, 'productivity')
        prodBoost += db.getModuleAttribut(module3, 'productivity')
        prodBoost += db.getModuleAttribut(module4, 'productivity')
        return prodBoost
    
    def beaconBoostPR(self, amount, module):
        '''
        To calculate the boost of beacon's
        It is calculated with with just one module 
            --> no need to divide with 2 (Because beacon Boost)
        @return float pr%
        '''
        i = 0
        boost = 0
        while i < amount:
            boost += (self.moduleSpeedBoost(module))
            i += 1
        return boost
    
    '''
    # Testing Area
    # 
    # TESTING AREA
    # 
    # Testing Area
    '''
    def main(self):
        # ab = self.moduleProductivityBoost('speed-module-3', 'speed-module-3', 'speed-module-3', 'speed-module-3')
        # ab = self.builderFullBelt('accumulator', 'assembling-machine-3', 'productivity-module-3', 'productivity-module-3', 'productivity-module-3', 'productivity-module-3', 'speed-module-3', 4)
        # ab = self.builderPr('assembling-machine-3', 'productivity-module-3', 'productivity-module-3', 'productivity-module-3', 'productivity-module-3', 'speed-module-3', 4 )
        # return ab
        pass

if __name__ == "__main__":
    a = calcPR()
    db = getValues()
    # print(a.main())
