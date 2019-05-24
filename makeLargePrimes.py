#!/usr/bin/env python

import os

from primeDataUtils import readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    firstDataFile = 0
    lastDataFile = 950

    outputInterval = 100
    printInterval = 100000

    directory = 'g:\\primes'

    print( )

    largeFile = open( directory + os.sep + 'large_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 'g:\\primes', firstDataFile, lastDataFile ):
        if index < 1000000:
            continue

        if index == 10000000:
            outputInterval = 1000;

        if index % outputInterval == 0:
            largeFile.write( '{:12} {}\n'.format( index, prime ) )

        if index == 1000000000:
            break

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

    largeFile.close( )


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

