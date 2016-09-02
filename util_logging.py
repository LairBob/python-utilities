# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

import os

class clsLogger:
    
    def __init__( self, **logArgs ):
        
        # Create a per-instance dict to store local properties
        self._properties = {}
        self._properties[ 'root' ] = os.getcwd()
        self._properties[ 'logPath' ] = "\\logs"
        self._properties[ 'logName' ] = "log-out"
        self._properties[ 'logExt' ] = ".log"
        
        # Traverse through any kw arguments that were passed
        for logArg in logArgs:
            
            # If it's a "known" argument, then process it
            if logArg in self._properties:
                # Check if the property needs to be passed through its dedicated handler
                if logArg == "logPath":
                    self.logPath( logArgs[ logArg ] )
                else:                    
                    self._properties[ logArg ] = logArgs[ logArg ]
            else:
                raise Exception(" UKNOWN PROPERTY: "+logArgs[ logArg ])        
 
    # Dedicated method exposed to process path property   
    def logPath( self, *args ):
        if args:
            tmpPath = args[0]
            if tmpPath[0] != "\\":
                tmpPath = "\\"+tmpPath
            if tmpPath[-1] == "\\":
                tmpPath = tmpPath[:-1]
            self._properties[ 'logPath' ] = tmpPath
        return self._properties[ 'logPath' ]

    # Dedicated method exposed to process name property   
    def logName( self, *args ):
        if args:
            tmpName = args[0]
            if '.' in tmpName:
                self._properties[ 'logName' ] = tmpName.split('.')[0]
                self.logExt( '.'+tmpName.split('.')[1] )
            else:
                self._properties[ 'logName' ] = tmpName
        return self._properties[ 'logName' ]+self.logExt()

    # Dedicated method exposed to process extension property   
    def logExt( self, *args ):
        if args:
            self._properties[ 'logExt' ] = args[0]
        return self._properties[ 'logExt' ]



#%% Unit tests
 
if __name__ == '__main__':
    
    # Path tests
    tmpLogger = clsLogger( logPath = "path", logName = "log-main" )
    print ( tmpLogger.logPath() )
    print ( tmpLogger.logPath( '\\subleft' ) )
    print ( tmpLogger.logPath( '\\subboth\\' ) )
    print ( tmpLogger.logPath( 'subright\\' ) )
    print ( tmpLogger.logPath( 'subnone' ) )
    print ( tmpLogger.logPath() )
 
    print ( tmpLogger.logName() )
    print ( tmpLogger.logName( 'log-test' ) )
    print ( tmpLogger.logName( 'log-test.txt' ) )
    print ( tmpLogger.logName() )
   