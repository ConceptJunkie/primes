#!/usr/bin/env python

import os

from primeDataUtils import isPrime, readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    firstDataFile = 0
    lastDataFile = 50

    outputInterval = 100
    printInterval = 10000

    directory = 'g:\\primes'

    print( )

    smallFile = open( directory + os.sep + 'small_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 'g:\\primes', firstDataFile, lastDataFile ):

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

