#!/usr/bin/env python

import os

from primeDataUtils import outputDirectory, readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    firstDataFile = 0
    lastDataFile = 9950

    previousPrime = -9999999
    printInterval = 10000

    diffsFile = open( outputDirectory + os.sep + 'prime_diffs-{:05}-{:05}.txt'.format( firstDataFile, firstDataFile + 50 ), 'w' )

    print( )

    for index, prime in readPrimeNumbers( firstDataFile, lastDataFile ):
        if previousPrime == -9999999:
            previousPrime = prime
            continue

        diffsFile.write( '{},{}\n'.format( index - 1, prime - previousPrime ) )

        previousPrime = prime

        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        if index % 50000000 == 1:
            diffsFile.close( )

            fileNum = index // 1000000

            diffsFile = open( outputDirectory + os.sep + 'prime_diffs-{:05}-{:05}.txt'.format( fileNum, fileNum + 50 ), 'w' )

    diffsFile.close( )


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

