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

    primes = [ 0 ] * 8

    sexyPrimeIndex = 0
    sexyTripletIndex = 0
    sexyQuadIndex = 0

    sexyPrimeInterval = 1
    sexyTripletInterval = 1
    sexyQuadInterval = 1

    printInterval = 100000

    print( )

    sexyPrimeFile = open( outputDirectory + os.sep + 'sexy_primes.txt', 'w' )
    sexyTripletFile = open( outputDirectory + os.sep + 'sexy_triplets.txt', 'w' )
    sexyQuadFile = open( outputDirectory + os.sep + 'sexy_quadruplets.txt', 'w' )

    for index, prime in readPrimeNumbers( 60000000000 ):
        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        primes.append( prime )
        del primes[ 0 ]

        if primes[ 0 ] == 0:
            continue

        prime0 = primes[ 0 ]

        b6 = False
        b12 = False
        b18 = False

        for i in primes:
            if i == prime0 + 6:
                b6 = True
            elif i == prime0 + 12:
                b12 = True
            elif i == prime0 + 18:
                b18 = True
                break

        if not b6:
            continue

        # we found a sexy prime
        sexyPrimeIndex += 1

        if sexyPrimeIndex % sexyPrimeInterval == 0:
            sexyPrimeInterval = updateOutputInterval( sexyPrimeIndex, sexyPrimeInterval )
            sexyPrimeFile.write( '{:12} {}\n'.format( sexyPrimeIndex, prime0 ) )

        if b12:
            if b18:
                # we found a sexy quadruplet
                sexyQuadIndex += 1

                if sexyQuadIndex % sexyQuadInterval == 0:
                    sexyQuadInterval = updateOutputInterval( sexyQuadIndex, sexyQuadInterval )
                    sexyQuadFile.write( '{:12} {}\n'.format( sexyQuadIndex, prime0 ) )
            else:
                # we found a sexy triplet
                sexyTripletIndex += 1

                if sexyTripletIndex % sexyTripletInterval == 0:
                    sexyTripletInterval = updateOutputInterval( sexyTripletIndex, sexyTripletInterval )
                    sexyTripletFile.write( '{:12} {}\n'.format( sexyTripletIndex, prime0 ) )

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

