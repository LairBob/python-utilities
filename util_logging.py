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
        self._properties['indentLevel'] = 0
        self._properties['indentSize'] = 4

        self._logLevel = 2

        self._fM = fManager( **fArgs )

        self._currTime = strTimestamp

        self.write( "INITIATING LOG OUTPUT: "+strTimestamp, padBefore = 2, padAfter = 3 )

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


#%% Property management functions

    def indentLevel(self, *args):
        if args:
            self._properties['indentLevel'] = args[0]
        return self._properties['indentLevel']

    def indentSize(self, *args):
        if args:
            self._properties['indentSize'] = args[0]
        return self._properties['indentSize']

    def indent(self, **kwargs):

        if 'myLevel' in kwargs:
            indLevel = kwargs[ 'myLevel' ]
        else:
            indLevel = self._properties[ 'indentLevel' ]

        if 'mySize' in kwargs:
            indSize = kwargs[ 'mySize' ]
        else:
            indSize = self._properties[ 'indentSize' ]

        intIndent = indLevel * indSize

        return (" " * intIndent )

#%% File management functions

    def write(self, *args, **kwargs):

        if 'padBefore' in kwargs:
            try:
                for n in range(kwargs['padBefore']):
                    self._fM.write()
            except:
                pass


        if 'indentLevel' in kwargs:
            self.indentLevel( kwargs[ 'indentLevel' ] )

        if 'indentSize' in kwargs:
            self.indentSize( kwargs[ 'indentSize' ] )

        strIndent = self.indent( **kwargs )

        if args:
            tmpStr = strIndent+str(args[0])

        self._fM.write( tmpStr )


        if 'padAfter' in kwargs:
            try:
                for n in range(kwargs['padAfter']):
                    self._fM.write()
            except:
                pass


    def _lWrite(self, myLevel, *args):
        if args:
            if self._logLevels[ myLevel ] > self._logLevel:
                self.write( *args )




#%% Unit tests

if __name__ == '__main__':

    testBase = True
    testStress = False

#%% Base tests

    if testBase:
        tmpLogger = clsLogger( fileName = "log-test", fileExt = "log" )
        tmpLogger.write( 'Testing' )
        tmpLogger.write( 'Indent 01', indentLevel = 1 )
        tmpLogger.write( 'Indent 02', indentLevel = 2, padBefore = 1, padAfter = 2 )
        tmpLogger.write( 'Testing Level 02' )
        tmpLogger.write( 'Testing Temp Level', myLevel = 0 )
        tmpLogger.write( 'Testing Level 02' )




#%% Stress tests


    if testStress:
        pass