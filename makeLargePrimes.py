#!/usr/bin/env python

import os

from primeDataUtils import outputDirectory, readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    outputInterval = 100
    printInterval = 100000

    print( )

    largeFile = open( outputDirectory + os.sep + 'large_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 1000000000 ):
        if index < 1000000:
            continue

        if index == 10000000:
            outputInterval = 1000;

        if index % outputInterval == 0:
            largeFile.write( '{:12} {}\n'.format( index, prime ) )

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

