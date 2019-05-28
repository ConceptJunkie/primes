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

    primes = [ 0 ] * 8

    sexyPrimeIndex = 0
    sexyTripletIndex = 0
    sexyQuadIndex = 0

    sexyPrimeIndex = 1
    sexyTripletIndex = 1
    sexyQuadIndex = 1

    sexyPrimeInterval = 1
    sexyTripletInterval = 1
    sexyQuadInterval = 1

    printInterval = 100000

    print( )

    sexyPrimeFile = open( outputDirectory + os.sep + 'sexy_primes.txt', 'w' )
    sexyTripletFile = open( outputDirectory + os.sep + 'sexy_triplets.txt', 'w' )
    sexyQuadFile = open( outputDirectory + os.sep + 'sexy_quadruplets.txt', 'w' )

    for index, prime in readPrimeNumbers( ):
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

        if sexyPrimeIndex % sexyPrimeInterval == 0:
            if sexyPrimeIndex == 100:
                sexyPrimeInterval = 10
            elif sexyPrimeIndex == 10000:
                sexyPrimeInterval = 100
            elif sexyPrimeIndex == 100000:
                sexyPrimeInterval = 1000
            elif sexyPrimeIndex == 1000000:
                sexyPrimeInterval = 10000
            elif sexyPrimeIndex == 10000000:
                sexyPrimeInterval = 100000

            sexyPrimeFile.write( '{:12} {}\n'.format( sexyPrimeIndex, prime - 6 ) )

        if b12:
            if b18:
                # we found a sexy quadruplet
                sexyQuadIndex += 1

                if sexyQuadIndex % sexyQuadInterval == 0:
                    if sexyQuadIndex == 100:
                        sexyQuadInterval = 10
                    elif sexyQuadIndex == 100000:
                        sexyQuadInterval = 100
                    elif sexyQuadIndex == 1000000:
                        sexyQuadInterval = 1000
                    elif sexyQuadIndex == 10000000:
                        sexyQuadInterval = 10000

                    sexyQuadFile.write( '{:12} {}\n'.format( sexyQuadIndex, prime - 18 ) )  # 18 because 3 * 6
            else:
                # we found a sexy triplet
                sexyTripletIndex += 1

                if sexyTripletIndex % sexyTripletInterval == 0:
                    if sexyTripletIndex == 100:
                        sexyTripletInterval = 10
                    elif sexyTripletIndex == 10000:
                        sexyTripletInterval = 100
                    elif sexyTripletIndex == 100000:
                        sexyTripletInterval = 1000
                    elif sexyTripletIndex == 1000000:
                        sexyTripletInterval = 10000
                    elif sexyTripletIndex == 10000000:
                        sexyTripletInterval = 100000

                    sexyTripletFile.write( '{:12} {}\n'.format( sexyTripletIndex, prime - 12 ) )  # 12 because 2 * 6

    sexyPrimeFile.close( )
    sexyTripletFile.close( )
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

