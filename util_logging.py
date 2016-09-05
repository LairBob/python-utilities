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

        self._logLevel = 'WARNING'

        self._fM = fManager( **fArgs )

        self._currTime = strTimestamp

        self.write( "INITIATING LOG OUTPUT: "+strTimestamp, padBefore = 1, padAfter = 1 )

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


#%% File output functions

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

        strPrefix = ""
        if 'prefix' in kwargs:
            strPrefix = kwargs[ 'prefix' ]+": "

        if args:
            tmpStr = strIndent+strPrefix+str(args[0])

        self._fM.write( tmpStr )


        if 'padAfter' in kwargs:
            try:
                for n in range(kwargs['padAfter']):
                    self._fM.write()
            except:
                pass

#%% Logging level functions

    def loggingLevel(self, *args):
        # Check to see if an argument has been passed
        if args:
            # Check to see whether the argument is in the list of 'known' logging level labels ('INFO', 'ERROR', etc.)
            if args[0] in self._logLevels:
                # If it is in the list, set this instance's new minimal logging threshold to the new value
                self._logLevel = args[0]
            else:
                # If it's not in the list, raise and exception
                raise Exception("ERROR: Attempt to set log level to: "+args[0])
        return self._logLevel

    def _lWrite(self, myLevel, *args, **kwargs):
        if args:
            if self._logLevels[ myLevel ] >= self._logLevels[ self._logLevel ]:
                self.write( *args, **kwargs, prefix = myLevel )

    def DEBUG(self, *args, **kwargs):
        self._lWrite( 'DEBUG', *args, **kwargs )

    def INFO(self, *args, **kwargs):
        self._lWrite( 'INFO', *args, **kwargs )

    def WARNING(self, *args, **kwargs):
        self._lWrite( 'WARNING', *args, **kwargs )

    def ERROR(self, *args, **kwargs):
        self._lWrite( 'ERROR', *args, **kwargs )

    def CRITICAL(self, *args, **kwargs):
        self._lWrite( 'CRITICAL', *args, **kwargs )



#%% Unit tests

if __name__ == '__main__':

    testBase = False
    testLevels = True
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

#%% Logging level tests

    if testLevels:
        tmpLogger = clsLogger( fileName = "log-test", fileExt = "log" )

        tmpLogger.DEBUG( "Test" )
        tmpLogger.INFO( "Test" )
        tmpLogger.WARNING( "Test" )
        tmpLogger.ERROR( "Test" )
        tmpLogger.CRITICAL( "Test" )

        tmpLogger.write("New Threshold: "+tmpLogger.loggingLevel( 'DEBUG'), padBefore = 1, padAfter = 1 )

        tmpLogger.DEBUG( "Test" )
        tmpLogger.INFO( "Test" )
        tmpLogger.WARNING( "Test" )
        tmpLogger.ERROR( "Test" )
        tmpLogger.CRITICAL( "Test" )


#%% Stress tests


    if testStress:
        pass