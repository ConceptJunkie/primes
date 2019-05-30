#!/usr/bin/env python

import os

from primeDataUtils import outputDirectory, readPrimeNumbers, updateOutputInterval


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    lineCount = 1

    primesSize = 5

    primes = [ ]
    diffs = [ ]
    adiffs = [ ]

    for i in range( 0, primesSize ):
        primes.append( [ -9999999, -9999999 ] )

    for i in range( 0, primesSize - 1 ):
        diffs.append( 0 )
        adiffs.append( 0 )

    isolatedIndex = 0

    numberOfTypes = 100

    isolatedIndex = [ 0 ] * numberOfTypes
    isolatedFile = [ ]

    for i in range( 0, numberOfTypes ):
        isolatedFile.append( open( outputDirectory + os.sep + 'isolated{:03}_primes.txt'.format( i * 2 + 4 ), 'w' ) )

    printInterval = 100000

    outputInterval = [ 1 ] * numberOfTypes

    for index, prime in readPrimeNumbers( 1000000000 ):
        primes.append( [ index, prime ] )
        del primes[ 0 ]

        diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
        del diffs[ 0 ]

        sum = 0

        for i in range( 0, primesSize - 1 ):
            sum += diffs[ i ]
            adiffs[ i ] = sum

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        for i in range( 0, numberOfTypes ):
            diff = i * 2 + 4

            if diffs[ 0 ] > diff and diffs[ 1 ] > diff:
                isolatedIndex[ i ] += 1
                outputInterval[ i ] = updateOutputInterval( isolatedIndex[ i ], outputInterval[ i ] )
                isolatedFile[ i ].write( '{},{}\n'.format( isolatedIndex[ i ], primes[ 1 ][ 1 ] ) )

    for i in range( 0, numberOfTypes ):
        isolatedFile[ i ].close( )


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

