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
    lastDataFile = 1950

    sophieIndex = 0

    outputInterval = 100

    printInterval = 100000

    print( )

    sophieFile = open( outputDirectory + os.sep + 'sophie_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( firstDataFile, lastDataFile ):
        sophie = int( ( prime - 1 ) / 2 )

        if isPrime( sophie ):
            sophieIndex += 1

            if sophieIndex % outputInterval == 0:
                sophieFile.write( '{:12} {}\n'.format( sophieIndex, sophie ) )

                if sophieIndex == 1000000:
                    outputInterval = 1000
                elif sophieIndex == 10000000:
                    outputInterval = 10000

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

    sophieFile.close( )


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
