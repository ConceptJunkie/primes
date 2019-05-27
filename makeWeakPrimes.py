#!/usr/bin/env python

import os

from primeDataUtils import outputDirectory, readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    lineCount = 1

    howWeak = 10
    maxIndex = 1000000
    primesSize = howWeak + 2

    primes = [ ]
    diffs = [ ]

    # everything is offset by 2
    WeakIndex = [ 0 ] * 9

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

    WeakFiles = [ ]

    for i in range( 2, howWeak + 1 ):
        WeakFiles.append( open( outputDirectory + os.sep + 'weak_primes_{:02}.txt'.format( i ), 'w' ) )

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
                    print( '\r{:,}'.format( index ), end='' )

                #if primes[ 0 ][ 0 ] > 10000000:
                #    break

                if diffs[ 0 ] < diffs[ 1 ]:
                    for i in range( 1, howWeak ):
                        if diffs[ i ] < diffs[ i + 1 ]:
                            if primes[ 1 ][ 1 ] > 0 and WeakIndex[ i - 1 ] < maxIndex:
                                WeakIndex[ i - 1 ] += 1
                                WeakFiles[ i - 1 ].write( '{},{}\n'.format( WeakIndex[ i - 1 ], primes[ 1 ][ 1 ] ) )
                        else:
                            break

    for i in range( 2, howWeak + 1 ):
        WeakFiles[ i - 2 ].close( )


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

