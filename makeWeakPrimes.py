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

    howWeak = 10
    primesSize = howWeak + 2

    primes = [ ]
    diffs = [ ]

    # everything is offset by 2
    weakIndex = [ 0 ] * ( howWeak - 1 )
    outputIntervals = [ 1 ] * ( howWeak - 1 )

    for i in range( 0, primesSize ):
        primes.append( [ -9999999, -9999999 ] )

    for i in range( 0, primesSize - 1 ):
        diffs.append( 0 )

    weakFiles = [ ]

    for i in range( 2, howWeak + 1 ):
        weakFiles.append( open( outputDirectory + os.sep + 'weak_primes_{:02}.txt'.format( i ), 'w' ) )

    printInterval = 1000000

    for index, prime in readPrimeNumbers( 60000000000 ):
        primes.append( [ index, prime ] )
        del primes[ 0 ]

        diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
        del diffs[ 0 ]

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        if diffs[ 0 ] < diffs[ 1 ]:
            for i in range( 1, howWeak ):
                if diffs[ i ] < diffs[ i + 1 ]:
                    if primes[ 1 ][ 1 ] > 0:
                        weakIndex[ i - 1 ] += 1

                        if weakIndex[ i - 1 ] % outputIntervals[ i - 1 ] == 0:
                            outputIntervals[ i - 1 ] = updateOutputInterval( weakIndex[ i - 1 ], outputIntervals[ i - 1 ] )
                            weakFiles[ i - 1 ].write( '{:12} {}\n'.format( weakIndex[ i - 1 ], primes[ 1 ][ 1 ] ) )
                else:
                    break

    for i in range( 2, howWeak + 1 ):
        weakFiles[ i - 2 ].close( )


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

