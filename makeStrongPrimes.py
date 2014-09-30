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

    howStrong = 10
    maxIndex = 1000000
    primesSize = howStrong + 2

    primes = [ ]
    diffs = [ ]

    # everything is offset by 2
    strongIndex = [ 0 ] * 9

    for i in range( 0, primesSize ):
        primes.append( [ -9999999, -9999999 ] )

    for i in range( 0, primesSize - 1 ):
        diffs.append( 0 )

    firstDataFile = 0
    lastDataFile = 950

    inputList = [ ]

    current = firstDataFile

    while current <= lastDataFile:
        inputList.append( 'c:\\data\primes\\{:04}-{:04}.txt'.format( current, current + 50 ) )
        current += 50

    strongFiles = [ ]

    for i in range( 2, howStrong + 1 ):
        strongFiles.append( open( 'c:\\data\primes\\strong{:02}_primes.txt'.format( i ), 'w' ) )

    printInterval = 1000000

    for fileName in inputList:
        with open( fileName, 'r' ) as file:
            for line in file:
                items = line[ : -1 ].split( ',' )

                primes.append( [ int( items[ 0 ] ), int( items[ 1 ] ) ] )
                del primes[ 0 ]

                diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
                del diffs[ 0 ]

                sum = 0

                if primes[ 0 ][ 0 ] % printInterval == 0:
                    print( 'strong: {:,}'.format( primes[ 0 ][ 0 ] ) )

                #if primes[ 0 ][ 0 ] > 10000000:
                #    break

                if diffs[ 0 ] < diffs[ 1 ]:
                    for i in range( 1, howStrong ):
                        if diffs[ i ] > diffs[ i + 1 ]:
                            if primes[ 1 ][ 1 ]> 0 and strongIndex[ i - 1 ] < maxIndex:
                                strongIndex[ i - 1 ] += 1
                                strongFiles[ i - 1 ].write( '{},{}\n'.format( strongIndex[ i - 1 ], primes[ 1 ][ 1 ] ) )
                        else:
                            break

    for i in range( 2, howStrong + 1 ):
        strongFiles[ i - 2 ].close( )


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
