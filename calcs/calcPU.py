# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:07:21 2020

@author: freya
"""

from getValues import getValues

class calcPU():
    
    def __init__(self):
        # Connection to DataBase
        self.db = getValues()
        
        # speed-modul (v=speed increas) (e=electricity increas)
        self.sm1e = 0.5
        self.sm2e = 0.6
        self.sm3e = 0.7
        
        # electricity-modul (e=electricity increas)
        self.em1e = -0.3
        self.em2e = -0.4
        self.em3e = -0.5
        
        # productivity-modul (v=speed increas) (e=electricity increas) (p=productivity increas)
        self.pm1e = 0.4
        self.pm2e = 0.6
        self.pm3e = 0.8
    
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
    pass