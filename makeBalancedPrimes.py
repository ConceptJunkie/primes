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

    numberOfTypes = 6

    primesSize = numberOfTypes * 2 + 1
    center = primesSize // 2 - 1

    primes = [ ]
    diffs = [ ]

    for i in range( 0, primesSize ):
        primes.append( [ -9999999, -9999999 ] )

    for i in range( 0, primesSize - 1 ):
        diffs.append( 0 )

    firstDataFile = 0
    lastDataFile = 950

    balancedIndex = [ 0 ] * numberOfTypes
    balancedFile = [ ]

    for i in range( 0, numberOfTypes ):
        balancedFile.append( open( outputDirectory + os.sep + 'balanced{:02}_primes.txt'.format( i + 1 ), 'w' ) )

    printInterval = 100000
    outputInterval = 100

    for index, prime in readPrimeNumbers( firstDataFile, lastDataFile ):
        primes.append( [ index, prime ] )
        del primes[ 0 ]

        diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
        del diffs[ 0 ]

        sum = 0

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        for i in range( 0, numberOfTypes ):
            skip = False

            for j in range( 0, i + 1 ):
                if ( diffs[ center - j ] != diffs[ center + j + 1 ] ):
                    skip = True
                    break

            if skip:
                continue

            if primes[ center - i ][ 1 ] > 0:
                balancedIndex[ i ] += 1

                if balancedIndex[ i ] == 1000000:
                    outputInterval = 1000

                if balancedIndex[ i ] % outputInterval:
                    balancedFile[ i ].write( '{:12} {}\n'.format( balancedIndex[ i ], primes[ center - i ][ 1 ] ) )

    for i in range( 0, numberOfTypes ):
        balancedFile[ i ].close( )


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

