#!/usr/bin/python
# -*- coding: utf-8 -*-

import Config

class Humidity:

    def __init__(self):
        self.__cfg = Config.Config()
        self.__params = self.__cfg.getParameters()
        self.__path = self.__params['path']

    def getTemperature(self):
        tempFilePath = self.__path + self.__params['t_file']
        with open(tempFilePath,'r') as tempFile:
            return float(tempFile.read().strip())

    def getVdd(self):
        vddFilePath = self.__path + self.__params['vdd_file']
        with open(vddFilePath, 'r') as vddFile:
            return float(vddFile.read().strip())
        
    def getVac(self):
        vacFilePath = self.__path + self.__params['vac_file']
        with open(vacFilePath, 'r') as vacFile:
            return float(vacFile.read().strip())

    def getHumidity(self, perc=False, res=4):
        
        rh = float((self.getVac()/self.getVdd() - 0.16) / (0.062*(1.0546 - 0.00216*self.getTemperature())))
        
        if perc:
            return(round(rh*100,res))
        else:
            return(round(rh,res))
         

if __name__ == '__main__':
    
    h = Humidity()
    
    print "Temperature:\t %s°C" % h.getTemperature()
    print "Vdd:\t\t %s V" % h.getVdd()
    print "Vac:\t\t %s V" % h.getVac()
    print "Humidity:\t %s" % h.getHumidity()
    print "Humidity: \t %s%%" % h.getHumidity(perc=True,res=2)
