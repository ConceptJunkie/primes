#!/usr/bin/env python

import os

from primeDataUtils import outputDirectory, readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    firstDataFile = 30000
    lastDataFile = 39950

    outputInterval = 25000
    printInterval = 100000

    print( )

    hugeFile = open( outputDirectory + os.sep + 'huge_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( firstDataFile, lastDataFile ):
        if index % outputInterval == 0:
            hugeFile.write( '{:12} {}\n'.format( index, prime ) )

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

    hugeFile.close( )


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

