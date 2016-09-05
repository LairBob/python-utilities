# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

import os


class fWriter:

    def __init__(self, fManager):

        self._fM = fManager
#        print()
#        print(" ----- Constructing fWriter -----")
#
#        print("     AbsLoc: "+self._fM.absLoc())
        if not os.path.isdir(self._fM.absLoc()):
            print("          CREATING ABSLOC")
        # Ensure that the corresponding destination directory exists
        os.makedirs(self._fM.absLoc(), exist_ok=True)

        print("     fileName: "+self._fM.fileName())

        self._fOut = open(self._fM.absPath(), 'w', newline="\n")
#        with open(self._fM.absLoc() , self._fM.fileName(), 'w', newline='') as _fOut:
#            _fOut.write("Test")

    def write(self, *args):
#         print("---- OUT: "+strOut)
        if args:
            self._fOut.write(args[0]+'\n')
        else:
            self._fOut.write('\n')
        self._fOut.flush()




#%% CLASS

class fManager:

#%% Class constructor

    def __init__(self, **fileArgs):

        # Create a per-instance dict to store local properties
        self._properties = {}
        self._properties['root'] = os.getcwd()
        self._properties['relLoc'] = { "logs" }
        self._properties['fileName'] = "log-main"
        self._properties['fileExt'] = ".log"
        self._isMutable = False

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
                elif fileArg == "isMutable":
                    self._isMutable(fileArgs[fileArg])
                else:
                    self._properties[fileArg] = fileArgs[fileArg]
            else:
                raise Exception(" UKNOWN PROPERTY: "+fileArgs[fileArg])

        self._fWriter = fWriter(self)


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


#%% File I/O functions

    def write(self, *args):
        self._fWriter.write( *args )



#%% Unit tests

if __name__ == '__main__':

    testPaths = False
    testStress = False
    testFileOut = True


#%% Path tests

    if testPaths:
        tmpPaths = fManager(relLoc="\\logs", fileName="log-main")

        print("Root: "+tmpPaths.root())
        print("relLoc: "+tmpPaths.relLoc())
        print("absLoc: "+tmpPaths.absLoc())

        print("fileName: "+tmpPaths.fileName())
        print("fileExt: "+tmpPaths.fileExt())

        print("relPath: "+tmpPaths.relPath())
        print("absPath: "+tmpPaths.absPath())

        print("New relLoc: "+tmpPaths.relLoc( "newtestdir\\newtestsub\\" ))
        print("New relPath: "+tmpPaths.relPath())
        print("New absPath: "+tmpPaths.absPath())


#%% Stress tests

    if testStress:
        tmpPaths = fManager(relLoc="\\test-logs", fileName="log-test")

        print(tmpPaths.relLoc('\\test-left'))
        print(tmpPaths.relLoc('\\test-both\\'))
        print(tmpPaths.relLoc('test-right\\'))
        print(tmpPaths.relLoc('test-none'))
        print(tmpPaths.relLoc('test-parent\\test-child'))

        print(tmpPaths.fileName('log-test'))
        print(tmpPaths.fileName('log-test.txt'))
        print(tmpPaths.fileExt('.csv'))
        print(tmpPaths.fileExt('txt'))


#%% File output tests

    if testFileOut:
        tmpWriteTest = fManager()
        tmpWriteTest.write("sadasdasd")
