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

    primes = [ 0 ] * 8

    sexyPrimeIndex = 0
    sexyTripletIndex = 0
    sexyQuadIndex = 0

    firstDataFile = 0
    lastDataFile = 950

    outputInterval = 100
    printInterval = 100000

    directory = 'g:\\primes'

    print( )

    sexyPrimeFile = open( directory + os.sep + 'sexy_primes.txt', 'w' )
    sexyTripletFile = open( directory + os.sep + 'sexy_triplets.txt', 'w' )
    sexyQuadFile = open( directory + os.sep + 'sexy_quadruplets.txt', 'w' )

    for index, prime in readPrimeNumbers( 'g:\\primes', firstDataFile, lastDataFile ):
        if index == 1000000000:
            outputInterval = 1000

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        primes.append( prime )
        del primes[ 0 ]

        b6 = False
        b12 = False
        b18 = False

        for i in primes[ : : -1 ]:
            if not b6 and i == prime - 6:
                b6 = True

            if not b12 and i == prime - 12:
                b12 = True

            if i == prime - 18:
                b18 = True
                break

        if not b6:
            continue

        # we found a sexy prime
        sexyPrimeIndex += 1

        if sexyPrimeIndex % outputInterval == 0:
            sexyPrimeFile.write( '{:12} {}\n'.format( sexyPrimeIndex, prime - 6 ) )

        if b12:
            if b18:
                # we found a sexy quadruplet
                sexyQuadIndex += 1

                if sexyQuadIndex % outputInterval == 0:
                    sexyQuadFile.write( '{:12} {}\n'.format( sexyQuadIndex, prime - 18 ) )  # 18 because 3 * 6
            else:
                # we found a sexy triplet
                sexyTripletIndex += 1

                if sexyTripletIndex % outputInterval == 0:
                    sexyTripletFile.write( '{:12} {}\n'.format( sexyTripletIndex, prime - 12 ) )  # 12 because 2 * 6

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

