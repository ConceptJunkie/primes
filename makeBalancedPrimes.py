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

    numberOfTypes = 3

    primesSize = numberOfTypes * 2 + 1
    center = numberOfTypes - 1

    #print( 'size', primesSize )
    #print( 'center', center )

    primes = [ ]
    diffs = [ ]

    for i in range( 0, primesSize ):
        primes.append( [ 0, 0 ] )

    for i in range( 0, primesSize - 1 ):
        diffs.append( 0 )

    balancedIndex = [ 0 ] * numberOfTypes
    outputInterval = [ 1 ] * numberOfTypes
    balancedFile = [ ]

    for i in range( 0, numberOfTypes ):
        balancedFile.append( open( outputDirectory + os.sep + 'balanced{:02}_primes.txt'.format( i + 1 ), 'w' ) )

    printInterval = 100000

    for index, prime in readPrimeNumbers( 1000000000 ):
        primes.append( [ index, prime ] )
        del primes[ 0 ]

        diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
        del diffs[ 0 ]

        # wait until our data structure is filled with actual data
        if diffs[ 0 ] == 0:
            continue

        sum = 0

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        #print( diffs, prime )

        for i in range( 0, numberOfTypes ):
            skip = False

            for j in range( 0, i + 1 ):
                if ( diffs[ center - j ] != diffs[ center + j + 1 ] ):
                    skip = True
                    break

            if skip:
                continue

            if primes[ center ][ 1 ] > 0:
                balancedIndex[ i ] += 1

                if balancedIndex[ i ] % outputInterval[ i ] == 0:
                    outputInterval[ i ] = updateOutputInterval( balancedIndex[ i ], outputInterval[ i ] )
                    #print( 'balanced', i, 'prime', primes[ center + 1 ][ 1 ] )
                    balancedFile[ i ].write( '{:12} {}\n'.format( balancedIndex[ i ], primes[ center + 1 ][ 1 ] ) )

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

