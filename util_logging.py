# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

from util_file_managers import fManager
from config_main import strTimestamp

class clsLogger:

#%% Class constructor

    def __init__( self, **fArgs ):

        self._properties = {}
        self._properties['indent'] = 0
        self._properties['indentSize'] = 4

        self._fM = fManager( **fArgs )

        self._currTime = strTimestamp

        self.write( "BEGINNING LOG OUTPUT: "+strTimestamp )

        for fArg in fArgs:
            if fArg == 'strHeader':
                self.write( fArg[ 'strHeader' ])
            else:
                self._properties[ fArg ] = fArgs[ fArg ]

    def write(self, strOut):
        self._fM.write( strOut )

#%% File management functions



#%% Unit tests

if __name__ == '__main__':

    testBase = True
    testStress = False

#%% Base tests

    if testBase:
        tmpLogger = clsLogger( fileName = "log-test", fileExt = "log" )



#%% Stress tests


    if testStress:
        pass