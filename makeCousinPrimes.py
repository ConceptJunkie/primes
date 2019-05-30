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

    diff = 0

    cousinIndex = 0
    outputInterval = 1

    printInterval = 100000

    previousPrime = 1

    print( )

    cousinFile = open( outputDirectory + os.sep + 'cousin_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 4000000000 ):
        diff = prime - previousPrime

        previousPrime = prime

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        if diff == 4:
            cousinIndex += 1

            if cousinIndex % outputInterval == 0:
                outputInterval = updateOutputInterval( cousinIndex, outputInterval )
                cousinFile.write( '{:12} {}\n'.format( cousinIndex, prime - 4 ) )

    cousinFile.close( )


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

