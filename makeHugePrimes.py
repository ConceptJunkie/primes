#!/usr/bin/env python

import os

from primeDataUtils import readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    firstDataFile = 15000
    lastDataFile = 29950

    outputInterval = 25000
    printInterval = 100000

    directory = 'g:\\primes'

    print( )

    hugeFile = open( directory + os.sep + 'huge_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 'g:\\primes', firstDataFile, lastDataFile ):
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

