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

    diffs = [ 0 ] * 3

    sexyQuadIndex = 0

    firstDataFile = 0
    lastDataFile = 50

    outputInterval = 100
    printInterval = 100000

    previousPrime = 1

    directory = 'g:\\primes'

    print( )

    sexyQuadFile = open( directory + os.sep + 'sexy_quadruplets.txt', 'w' )

    for index, prime in readPrimeNumbers( 'g:\\primes', firstDataFile, lastDataFile ):
        if index == 1000000000:
            outputInterval = 1000

        diffs.append( prime - previousPrime )
        del diffs[ 0 ]

        previousPrime = prime

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        if diffs == [ 6, 6, 6 ]:
            sexyQuadIndex += 1

            if sexyQuadIndex % outputInterval == 0:
                sexyQuadFile.write( '{} {}\n'.format( sexyQuadIndex, prime - 18 ) )  # 18 because 3 * 6

    sexyQuadFile.close( )


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

