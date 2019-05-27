#!/usr/bin/env python

import os

from primeDataUtils import isPrime, outputDirectory, readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    firstDataFile = 0
    lastDataFile = 0

    outputInterval = 100
    printInterval = 10000

    print( )

    smallFile = open( outputDirectory + os.sep + 'small_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( ):
        if index == 100000:
            outputInterval = 200
        elif index == 300000:
            outputInterval = 500
        elif index > 1000000:
            break

        if index % outputInterval == 0 or ( isPrime( index ) and index > 500 ):
            smallFile.write( '{:12} {}\n'.format( index, prime ) )

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

    smallFile.close( )


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

