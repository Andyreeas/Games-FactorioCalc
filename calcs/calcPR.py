# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 01:41:41 2020

@author: freya
"""

from getValues import getValues

class calcPR():
    
    '''
    Variabels for Modules
    '''
    def __init__(self):
        # Connection to DataBase
        self.db = getValues()
        
        # speed-modul (v=speed increas)
        self.sm1v = 0.2
        self.sm2v = 0.3
        self.sm3v = 0.5
        
        # productivity-modul (v=speed increas) (e=electricity increas) (p=productivity increas)
        self.pm1v = -0.15
        self.pm1p = 0.04
        self.pm2v = -0.15
        self.pm2p = 0.06
        self.pm3v = -0.15
        self.pm3p = 0.10
        
        # production rate
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
        
        self.yellowBelt = 15
        self.redBelt = 30
        self.blueBelt = 45

    def builderAmount(self, itemsneededperMinute, item, builder, smXv1, smXv2, smXv3, smXv4, number, beasmXv1, beasmXv2, pmXp1, pmXp2, pmXp3, pmXp4):
        '''
        returns Amount of Builders needed to produce itemsneededperMinute
        '''
        ips = self.itemsPerSecond(item, builder, smXv1, smXv2, smXv3, smXv4, number, beasmXv1, beasmXv2, pmXp1, pmXp2, pmXp3, pmXp4)
        amountBuilder = itemsneededperMinute / (ips * 60)
        return amountBuilder
    
    def builderFullBelt(self, belt, item, builder, smXv1, smXv2, smXv3, smXv4, number, beasmXv1, beasmXv2, pmXp1, pmXp2, pmXp3, pmXp4):
        '''
        returns Amount of Builders needed to fill specific Belt
        param int belt
        '''
        ips = self.itemsPerSecond(item, builder, smXv1, smXv2, smXv3, smXv4, number, beasmXv1, beasmXv2, pmXp1, pmXp2, pmXp3, pmXp4)
        amountBuilder = belt / ips
        return amountBuilder
    
    def itemsPerSecond(self, item, builder, smXv1, smXv2, smXv3, smXv4, number, beasmXv1, beasmXv2, pmXp1, pmXp2, pmXp3, pmXp4):
        time = self.time(item, builder, smXv1, smXv2, smXv3, smXv4, number, beasmXv1, beasmXv2)
        amount = self.db.getAmount(item)
        ips = float(amount[1]) / time
        ips = ips * self.builderPD(pmXp1, pmXp2, pmXp3, pmXp4)
        return ips

    def time(self, item, builder, smXv1, smXv2, smXv3, smXv4, number, beasmXv1, beasmXv2):
        '''
        To calculate Time of item with boost
        !!! But productivity is not included !!!!
        '''
        time = float(self.db.getTime(item))
        pr = self.builderPR(builder, smXv1, smXv2, smXv3, smXv4)
        boost = self.beaconBoostPR(number, beasmXv1, beasmXv2)
        pr = builder + (builder * (pr + boost))
        time = time / pr
        return time
    
    def builderPR(self, builder, smXv1, smXv2, smXv3, smXv4):
        '''
        To calculate the Production rate of the builder
        @param builder (assembler, chem plant, usw..)
        @param modules 1 - 4 (Optional)
        return float pr
        '''
        prboost = smXv1 + smXv2 + smXv3 + smXv4
        return prboost
    
    def beaconBoostPR(self, number, smXv1, smXv2):
        '''
        To calculate the boost of beacon's
        @return float pr%
        '''
        i = 0
        boost = 0
        while i < number:
            boost = boost + smXv1 + smXv2
            i = i + 1
        return boost/2
    
    def builderPD(self, pmXp1, pmXp2, pmXp3, pmXp4):
        '''
        To calculate the Productivity of the modules in the builder
        '''
        pd = 1 + pmXp1 + pmXp2 + pmXp3 + pmXp4
        return pd
        
    '''
    # Testing Area
    # 
    # TESTING AREA
    # 
    # Testing Area
    '''
    def main(self):
        # print(self.time('advanced-circuit', 'true', self.assembler3))
        # pr = self.builderPR(self.assembler3, self.sm3v, self.sm3v, self.sm3v, self.sm3v)
        # time = self.time('accumulator', self.assembler3, self.pm3v, self.pm3v, self.pm3v, self.pm3v, 4,self.sm3v, self.sm3v)
        # ipm = self.itemsPerSecond('accumulator', self.assembler3, self.pm3v, self.pm3v, self.pm3v, self.pm3v, 8,self.sm3v, self.sm3v, self.pm3p, self.pm3p, self.pm3p, self.pm3p)
        # boostpr = self.beaconBoostPR(4, self.sm3v, self.sm3v)
        # ab = self.builderAmount(1000, 'military-science-pack', self.assembler3, self.pm3v, self.pm3v, self.pm3v, self.pm3v, 8,self.sm3v, self.sm3v, self.pm3p, self.pm3p, self.pm3p, self.pm3p)
        ab = self.builderFullBelt(self.blueBelt, 'copper-cable', self.assembler3, self.pm3v, self.pm3v, self.pm3v, self.pm3v, 8,self.sm3v, self.sm3v, self.pm3p, self.pm3p, self.pm3p, self.pm3p)
        return ab
        # return boostpr

if __name__ == "__main__":
    a = calcPR()
    print(a.main())

       