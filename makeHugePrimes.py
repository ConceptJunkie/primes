#!/usr/bin/env python

import os

from primeDataUtils import outputDirectory, readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    outputInterval = 25000
    printInterval = 100000

    print( )

    hugeFile = open( outputDirectory + os.sep + 'huge_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 60000000000 ):
        if index % outputInterval == 0:
            if index == 30000000000:
                outputInterval = 50000

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

