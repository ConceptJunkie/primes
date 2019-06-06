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

    primes = [ 0 ] * 4

    octyPrimeIndex = 0
    octyTripletIndex = 0
    octyQuadIndex = 0

    octyPrimeInterval = 1
    octyTripletInterval = 1
    octyQuadInterval = 1

    printInterval = 100000

    print( )

    octyPrimeFile = open( outputDirectory + os.sep + 'octy_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 10000000000 ):
        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        primes.append( prime )
        del primes[ 0 ]

        if primes[ 0 ] == 0:
            continue

        prime0 = primes[ 0 ]

        b8 = False

        for i in primes:
            if i == prime0 + 8:
                b8 = True
                break

        if not b8:
            continue

        # we found an octy prime
        octyPrimeIndex += 1

        if octyPrimeIndex % octyPrimeInterval == 0:
            octyPrimeInterval = updateOutputInterval( octyPrimeIndex, octyPrimeInterval )
            octyPrimeFile.write( '{:12} {}\n'.format( octyPrimeIndex, prime0 ) )

    octyPrimeFile.close( )


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

