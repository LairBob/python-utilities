# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

import os


class fManager:

#%% Class constructor

    def __init__(self, **fileArgs):

        # Create a per-instance dict to store local properties
        self._properties = {}
        self._properties['root'] = os.getcwd()
        self._properties['relLoc'] = { "dir" }
        self._properties['fileName'] = "new-file"
        self._properties['fileExt'] = ".txt"

        # Traverse through any kw arguments that were passed
        for fileArg in fileArgs:

            # If it's a "known" argument, then process it
            if fileArg in self._properties:
                # Check if the property needs to be passed through its dedicated handler
                if fileArg == "root":
                    self.root(fileArgs[fileArg])
                elif fileArg == "relLoc":
                    self.relLoc(fileArgs[fileArg])
                elif fileArg == "filename":
                    self.fileName(fileArgs[fileArg])
                elif fileArg == "fileExt":
                    self.fileExt(fileArgs[fileArg])
                else:                    
                    self._properties[fileArg] = fileArgs[fileArg]
            else:
                raise Exception(" UKNOWN PROPERTY: "+fileArgs[fileArg])        
 
 
 #%% Property interface functions
 
    # Dedicated method exposed to process root path property   
    def root(self, *args):
        if args:
            tmpRoot = args[0]
#            raise Exception("Changing Root: "+self._properties['root']+" --> "+tmpRoot)
            self._properties['root'] = tmpRoot
        return self._properties['root']

    # Dedicated method exposed to process path property   
    def relLoc(self, *args):
        if args:
            tmpPath = args[0]
            print("   Assigning relLoc: "+tmpPath)
#            raise Exception("Changing Path: "+os.path.join(*self._properties['relLoc'])+" --> "+tmpPath)

            self._properties['relLoc'] = tmpPath.split("\\")

        return os.path.join(*self._properties['relLoc'])

    def absLoc(self):
        return os.path.join(self.root(), self.relLoc())

    # Dedicated method exposed to process name property   
    def fileName(self, *args):
        if args:
            tmpName = args[0]
#            raise Exception("Changing Name: "+self._properties['fileName']+" --> "+tmpName)
            if '.' in tmpName:
                self._properties['fileName'] = tmpName.split('.')[0]
                self.fileExt('.'+tmpName.split('.')[1])
            else:
                self._properties['fileName'] = tmpName
        return self._properties['fileName']+self.fileExt()

    # Dedicated method exposed to process extension property   
    def fileExt(self, *args):
        if args:
            tmpExt = args[0]
#            raise Exception("Changing Extansion: "+self._properties['fileExt']+" --> "+tmpExt)
            if not tmpExt[0] == '.':
                tmpExt = '.'+tmpExt
            self._properties['fileExt'] = tmpExt
        return self._properties['fileExt']

    def relPath(self):
        return os.path.join(self.relLoc(), self.fileName())

    def absPath(self):
        return os.path.join(self.root(), self.relPath())



#%% Unit tests

if __name__ == '__main__':

    # Path tests
    tmpLogger = fManager(relLoc="path\\test\\logs", fileName="log-main")

    print("Root: "+tmpLogger.root())
    print("relLoc: "+tmpLogger.relLoc())
    print("absLoc: "+tmpLogger.absLoc())

    print("fileName: "+tmpLogger.fileName())
    print("fileExt: "+tmpLogger.fileExt())

    print("relPath: "+tmpLogger.relPath())
    print("absPath: "+tmpLogger.absPath())

    print("New relLoc: "+tmpLogger.relLoc( "newdir\\newsub\\" ))
    print("New relPath: "+tmpLogger.relPath())
    print("New absPath: "+tmpLogger.absPath())

#%% Stress tests

    testStress = False

    if testStress:
        print(tmpLogger.relLoc('\\subleft'))
        print(tmpLogger.relLoc('\\subboth\\'))
        print(tmpLogger.relLoc('subright\\'))
        print(tmpLogger.relLoc('subnone'))
        print(tmpLogger.relLoc('subpar\\subchild'))

        print(tmpLogger.fileName('log-test'))
        print(tmpLogger.fileName('log-test.txt'))
        print(tmpLogger.fileExt('.csv'))
        print(tmpLogger.fileExt('txt'))
