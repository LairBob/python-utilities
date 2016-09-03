# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

import os

class clsLogger:


#%% Class constructor
    
    def __init__( self, **logArgs ):
        
        # Create a per-instance dict to store local properties
        self._properties = {}
        self._properties[ 'root' ] = os.getcwd()
        self._properties[ 'relLoc' ] = [ "logs" ]
        self._properties[ 'logName' ] = "log-out"
        self._properties[ 'logExt' ] = ".log"
        
        # Traverse through any kw arguments that were passed
        for logArg in logArgs:
            
            # If it's a "known" argument, then process it
            if logArg in self._properties:
                # Check if the property needs to be passed through its dedicated handler
                if logArg == "relLoc":
                    self.relLoc( logArgs[ logArg ] )
                else:                    
                    self._properties[ logArg ] = logArgs[ logArg ]
            else:
                raise Exception(" UKNOWN PROPERTY: "+logArgs[ logArg ])        
 
 
 #%% Property interface functions
 
    # Dedicated method exposed to process root path property   
    def root( self, *args ):
        if args:
            tmpRoot = args[0]
#            raise Exception( "Changing Root: "+self._properties[ 'root' ]+" --> "+tmpRoot )
            self._properties[ 'root' ] = tmpRoot
        return self._properties[ 'root' ]

    # Dedicated method exposed to process path property   
    def relLoc( self, *args ):
        if args:
            tmpPath = args[0]
#            raise Exception( "Changing Path: "+os.path.join( *self._properties[ 'relLoc' ] )+" --> "+tmpPath )
            for eachSep in [ "\\", "/" ]:
                if eachSep in tmpPath:
                    self._properties[ 'relLoc' ] = tmpPath.split( eachSep )
                    break
        return os.path.join( *self._properties[ 'relLoc' ] )

    def absLoc( self ):
        return os.path.join( self.root(), self.relLoc() )

    # Dedicated method exposed to process name property   
    def logName( self, *args ):
        if args:
            tmpName = args[0]
#            raise Exception( "Changing Name: "+self._properties[ 'logName' ]+" --> "+tmpName )
            if '.' in tmpName:
                self._properties[ 'logName' ] = tmpName.split('.')[0]
                self.logExt( '.'+tmpName.split('.')[1] )
            else:
                self._properties[ 'logName' ] = tmpName
        return self._properties[ 'logName' ]+self.logExt()

    # Dedicated method exposed to process extension property   
    def logExt( self, *args ):
        if args:
            tmpExt = args[0]
#            raise Exception( "Changing Extansion: "+self._properties[ 'logExt' ]+" --> "+tmpExt )
            if not tmpExt[0] == '.':
                tmpExt = '.'+tmpExt
            self._properties[ 'logExt' ] = tmpExt
        return self._properties[ 'logExt' ]

    def relPath( self ):
        return os.path.join( self.relLoc(), self.logName() )

    def absPath( self ):
        return os.path.join( self.root(), self.relPath() )


#%% Unit tests
 
if __name__ == '__main__':
    
    # Path tests
    tmpLogger = clsLogger( relLoc = "path", logName = "log-main" )

    print ( tmpLogger.root() ) 
    print ( tmpLogger.relLoc() )
    print ( tmpLogger.absLoc() )

    print ( tmpLogger.logName() )
    print ( tmpLogger.logExt() )
    
    print ( tmpLogger.relPath() )
    print ( tmpLogger.absPath() )
 
    
#%% Stress tests

    testStress = False

    if testStress:
        print ( tmpLogger.relLoc( '\\subleft' ) )
        print ( tmpLogger.relLoc( '\\subboth\\' ) )
        print ( tmpLogger.relLoc( 'subright\\' ) )
        print ( tmpLogger.relLoc( 'subnone' ) )
        print ( tmpLogger.relLoc( 'subpar\\subchild' ) )
        
        print ( tmpLogger.logName( 'log-test' ) )
        print ( tmpLogger.logName( 'log-test.txt' ) )
        print ( tmpLogger.logExt( '.csv' ) )
        print ( tmpLogger.logExt( 'txt' ) )
