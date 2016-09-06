# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:28:14 2016

@author: lstanevich
"""

import util_logging
import datetime

logMain = util_logging.clsLogger( fileName = "log-main" )

#%% Function decorators

class EnterExitLog():
    def __init__(self, funcName):
        self.funcName = funcName

    def __enter__(self):
        logMain.indentRaise()
        logMain.DEBUG('Started: '+self.funcName)
        self.init_time = datetime.datetime.now()
        return self

    def __exit__(self, type, value, tb):
        logMain.DEBUG('Finished: %s in: %s seconds' % (self.funcName, datetime.datetime.now() - self.init_time))
        logMain.indentLower()

def dec_logEntryExit(func):
    def func_wrapper(*args, **kwargs):
        with EnterExitLog(func.__name__):
            return func(*args, **kwargs)

    return func_wrapper

class logDebugOverride():
    def __init__(self, funcName):
        self.funcName = funcName
        self._currLoggingLevel = logMain.loggingLevel()

    def __enter__(self):
        # logMain.loggingLevel( 'DEBUG' )
        logMain.indentRaise()
        logMain.DEBUG('DEBUG OVERRIDE: '+self.funcName, padBefore = 1)
        self.init_time = datetime.datetime.now()
        return self

    def __exit__(self, type, value, tb):
        logMain.DEBUG('FINISHED DEBUG OVERRIDE: %s in: %s seconds' % (self.funcName, datetime.datetime.now() - self.init_time))
        logMain.indentLower()
        logMain.loggingLevel( self._currLoggingLevel )

def dec_logDebugOverride(func):
    def func_wrapper(*args, **kwargs):
        with logDebugOverride(func.__name__):
            return func(*args, **kwargs)

    return func_wrapper



if __name__ == '__main__':

    logMain.loggingLevel( 'DEBUG' )

    @dec_logEntryExit
    def testFunc():
        print("TESTING")

    testFunc()