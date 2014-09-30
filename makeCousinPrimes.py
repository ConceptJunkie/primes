#!/usr/bin/env python

import contextlib
import bz2
import pickle


def saveFile( var, fileName ):
    with contextlib.closing( bz2.BZ2File( fileName + '.pckl.bz2', 'wb' ) ) as pickleFile:
        pickle.dump( var, pickleFile )


def loadFile( fileName ):
    with contextlib.closing( bz2.BZ2File( fileName + 'pckl.bz2', 'rb' ) ) as pickleFile:
        return pickle.load( pickleFile )


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    lineCount = 1

    primesSize = 11

    primes = [ ]
    diffs = [ ]
    adiffs = [ ]

    for i in range( 0, primesSize ):
        primes.append( [ -9999999, -9999999 ] )

    for i in range( 0, primesSize - 1 ):
        diffs.append( 0 )
        adiffs.append( 0 )

    cousinIndex = 0

    firstDataFile = 0
    lastDataFile = 950

    inputList = [ ]

    current = firstDataFile

    while current <= lastDataFile:
        inputList.append( 'c:\\data\primes\\{:04}-{:04}.txt'.format( current, current + 50 ) )
        current += 50

    for fileName in inputList:
        with open( fileName, 'r' ) as file:
            for line in file:
                items = line[ : -1 ].split( ',' )

                primes.append( [ int( items[ 0 ] ), int( items[ 1 ] ) ] )
                del primes[ 0 ]

                diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
                del diffs[ 0 ]

                sum = 0

                for i in range( 0, primesSize - 1 ):
                    sum += diffs[ i ]
                    adiffs[ i ] = sum

                if ( adiffs[ 0 ] == 4 ) or ( adiffs[ 1 ] == 4 ):
                    cousinIndex += 1
                    print( '{},{}'.format( cousinIndex, primes[ 0 ][ 1 ] ) )


#//******************************************************************************
#//
#//  __main__
#//
#//******************************************************************************

if __name__ == '__main__':
    try:
        main( )
    except KeyboardInterrupt:
        pass
