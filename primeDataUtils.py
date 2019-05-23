#!/usr/bin/env python

import os


#//******************************************************************************
#//
#//  readPrimeNumbers
#//
#//******************************************************************************

def readPrimeNumbers( directory, firstDataFile, lastDataFile ):
    inputList = [ ]

    current = firstDataFile

    while current <= lastDataFile:
        inputList.append( directory + os.sep + '{:05}-{:05}.txt'.format( current, current + 50 ) )
        current += 50

    for fileName in inputList:
        with open( fileName, 'r' ) as file:
            for line in file:
                items = line[ : -1 ].split( ',' )

                yield int( items[ 0 ] ), int( items[ 1 ] )


