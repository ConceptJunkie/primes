#!/usr/bin/env python

import os

from primeDataUtils import readPrimeNumbers


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
    strongIndex = [ 0 ] * ( howStrong - 1 )

    primes = [ [ -9999999, -9999999 ] ] * primesSize

    for i in range( 0, primesSize - 1 ):
        diffs = [ 0 ] * ( primesSize - 1 )

    firstDataFile = 0
    lastDataFile = 950

    directory = 'g:\\primes'

    print( )

    strongFiles = [ ]

    for i in range( 2, howStrong + 1 ):
        strongFiles.append( open( directory + os.sep + 'strong{:02}_primes.txt'.format( i ), 'w' ) )

    printInterval = 100000
    outputInterval = 100

    for index, prime in readPrimeNumbers( 'g:\\primes', firstDataFile, lastDataFile ):
        primes.append( [ index, prime ] )
        del primes[ 0 ]

        diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
        del diffs[ 0 ]

        sum = 0

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        if diffs[ 0 ] < diffs[ 1 ]:
            for i in range( 1, howStrong ):
                if diffs[ i ] > diffs[ i + 1 ]:
                    if primes[ 1 ][ 1 ] > 0 and strongIndex[ i - 1 ] < maxIndex:
                        strongIndex[ i - 1 ] += 1

                        if strongIndex[ i - 1 ] % outputInterval == 0:
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

