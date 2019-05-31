#!/usr/bin/env python

import os

from primeDataUtils import isPrime, outputDirectory, readPrimeNumbers, \
                           updateOutputInterval


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    sophieIndex = 0

    outputInterval = 1

    printInterval = 100000

    print( )

    sophieFile = open( outputDirectory + os.sep + 'sophie_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 4000000000 ):
        sophie = int( ( prime - 1 ) / 2 )

        if isPrime( sophie ):
            sophieIndex += 1

            if sophieIndex % outputInterval == 0:
                sophieFile.write( '{:12} {}\n'.format( sophieIndex, sophie ) )
                outputInterval = updateOutputInterval( sophieIndex, outputInterval )

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

