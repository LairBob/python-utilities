# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

from util_file_managers import fManager
from config_main import strTimestamp

class clsLogger:

#%% Class constructor

    _logLevels = { 'DEBUG' : 0, 'INFO' : 1, 'WARNING' : 2, 'ERROR' : 3, 'CRITICAL' : 4 }

    def __init__( self, **fArgs ):

        self._properties = {}
        self._properties['indent'] = 0
        self._properties['indentSize'] = 4

        self._logLevel = 2

        self._fM = fManager( **fArgs )

        self._currTime = strTimestamp

        self.write( "INITIATING LOG OUTPUT: "+strTimestamp )

        for fArg in fArgs:
            if fArg == 'strHeader':
                self.write( fArg[ 'strHeader' ])
            elif fArg == 'logLevel':
                if fArg[ 'logLevel' ] in self._logLevels:
                    self._logLevel = self._logLevels[ fArg[ 'logLevel' ] ]
                else:
                    raise Exception("ERROR: Attempt to set unknown Log Level: "+fArg[ 'logLevel' ])
            else:
                self._properties[ fArg ] = fArgs[ fArg ]

    def write(self, *args):
        if args:
            try:
                for n in range(args[1]):
                    self._fM.write()
            except:
                pass
        self._fM.write( *args )


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