# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

from util_file_managers import fManager


class clsLogger:

#%% Class constructor
    
    def __init__( self, **fArgs ):
        self.f = fManager( **fArgs )

#%% File management functions



#%% Unit tests
 
if __name__ == '__main__':
    
    # Path tests
    tmpLogger = clsLogger( relLoc = "path", fileName = "log-main" )

    print ( tmpLogger.f.root() ) 
    print ( tmpLogger.f.relLoc() )
    print ( tmpLogger.f.absLoc() )

    print ( tmpLogger.f.fileName() )
    print ( tmpLogger.f.fileExt() )
    
    print ( tmpLogger.f.relPath() )
    print ( tmpLogger.f.absPath() )
 
    
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
