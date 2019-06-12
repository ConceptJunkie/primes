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

    primesSize = 3

    primes = [ [ -9999999, -9999999 ] ] * primesSize
    diffs = [ 0 ] * ( primesSize - 1 )

    isolatedIndex = 0

    numberOfTypes = 100

    isolatedIndex = [ 0 ] * numberOfTypes
    outputInterval = [ 1 ] * numberOfTypes

    isolatedFiles = [ ]

    for i in range( 0, numberOfTypes ):
        isolatedFiles.append( open( outputDirectory + os.sep + 'isolated{:03}_primes.txt'.format( i * 2 + 4 ), 'w' ) )

    printInterval = 100000

    isolatedFiles[ 0 ].write( '{:12} {}\n'.format( 1, 2 ) )   # OEIS considers 2 an isolated prime
    isolatedIndex[ i ] += 1

    for index, prime in readPrimeNumbers( 60000000000 ):
        primes.append( [ index, prime ] )
        del primes[ 0 ]

        diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
        del diffs[ 0 ]

        sum = 0

        for i in range( 0, primesSize - 1 ):
            sum += diffs[ i ]

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        for i in range( 0, numberOfTypes ):
            diff = i * 2 + 4

            if ( diffs[ 0 ] >= diff ) and ( diffs[ 1 ] >= diff ):
                isolatedIndex[ i ] += 1

                if ( isolatedIndex[ i ] % outputInterval[ i ] == 0 ):
                    outputInterval[ i ] = updateOutputInterval( isolatedIndex[ i ], outputInterval[ i ] )
                    isolatedFiles[ i ].write( '{:12} {}\n'.format( isolatedIndex[ i ], primes[ 1 ][ 1 ] ) )

    for i in range( 0, numberOfTypes ):
        isolatedFiles[ i ].close( )


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

