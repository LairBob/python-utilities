# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

class clsLogger:
    
    _logPath = "\\logs"
    _logName = "log-out"
    _logExt = ".log"
    
    def __init__( self, **logArgs ):
        if "logPath" in logArgs:
            self.logPath ( logArgs[ 'logPath' ] )
        if "logName" in logArgs:
            self.logName ( logArgs[ 'logName' ] )
        if "logExt" in logArgs:
            self.logPath ( logArgs[ 'logExt' ] )
 
    def logPath( self, *args ):
        if args:
            tmpPath = args[0]
            if tmpPath[0] != "\\":
                tmpPath = "\\"+tmpPath
            if tmpPath[0] != "\\":
                tmpPath = tmpPath[:-1]
            self._logPath = tmpPath
        return self._logPath

    def logName( self, *args ):
        if args:
            self._logName = args[0]
        return self._logName+self.logExt()

    def logExt( self, *args ):
        if args:
            self._logExt = args[0]
        return self._logExt



#%% Unit tests
 
if __name__ == '__main__':
    
    # Path tests
    tmpLogger = clsLogger( logPath = "path", logName = "log-main" )
    print ( tmpLogger.logPath() )
    print ( tmpLogger.logPath( '\\sub' ) )
    print ( tmpLogger.logPath() )
 
    print ( tmpLogger.logName() )
    print ( tmpLogger.logName( 'log-test' ) )
    print ( tmpLogger.logName() )
   