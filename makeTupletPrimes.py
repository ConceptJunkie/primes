#!/usr/bin/env python

import os

from primeDataUtils import readPrimeNumbers


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    lineCount = 1

    primes = [ 0 ] * 8
    diffs = [ 0 ] * 7

    twinIndex = 0
    tripletIndex = 0
    quadIndex = 0
    quintIndex = 0
    sextIndex = 0

    firstDataFile = 0
    lastDataFile = 950

    twinInterval = 100
    tripletInterval = 100
    quadInterval = 1
    quintInterval = 1
    sextInterval = 1

    printInterval = 100000

    directory = 'g:\\primes'

    print( )

    twinFile = open( directory + os.sep + 'twin_primes.txt', 'w' )
    tripletFile = open( directory + os.sep + 'triplet_primes.txt', 'w' )
    quadFile = open( directory + os.sep + 'quad_primes.txt', 'w' )
    quintFile = open( directory + os.sep + 'quint_primes.txt', 'w' )
    sextFile = open( directory + os.sep + 'sext_primes.txt', 'w' )

    for index, prime in readPrimeNumbers( 'g:\\primes', firstDataFile, lastDataFile ):
        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        primes.append( prime )
        del primes[ 0 ]

        diffs.append( primes[ -1 ] - primes[ -2 ] )
        del diffs[ 0 ]

        # first check for twin primes
        if diffs[ -1 ] == 2:
            twinIndex += 1

            if twinIndex == 10000000:
                twinInterval = 300
            elif twinIndex == 100000000:
                twinInterval = 1000
            elif twinIndex == 1000000000:
                twinInterval = 3000
            elif twinIndex == 10000000000:
                twinInterval = 10000

            if twinIndex % twinInterval == 0:
                twinFile.write( '{:12} {}\n'.format( twinIndex, prime - 4 ) )

        # them check for a triplet
        if ( diffs[ -1 ] == 2 and diffs[ -2 ] == 4 ) or \
           ( diffs[ -1 ] == 4 and diffs[ -2 ] == 2 ):
            tripletIndex += 1

            if tripletIndex == 100000:
                tripletInterval = 500
            elif tripletIndex == 1000000:
                tripletInterval = 2000
            elif tripletIndex == 10000000:
                tripletInterval = 10000

            if tripletIndex % tripletInterval == 0:
                tripletFile.write( '{:12} {}\n'.format( tripletIndex, prime - 6 ) )

        # next, check for a quadruplet
        if ( prime - 19 ) % 30 == 0 and \
           diffs[ -1 ] == 2 and diffs[ -2 ] == 4 and diffs[ -3 ] == 2:
            quadIndex += 1

            if quadIndex == 100000:
                quadInterval = 5
            elif quadIndex == 1000000:
                quadInterval = 20
            elif quadIndex == 10000000:
                quadInterval = 100

            if quadIndex % quadInterval == 0:
                quadFile.write( '{:12} {}\n'.format( quadIndex, prime - 8 ) )

            if diffs[ -4 ] == 4:
                quintIndex += 1

                if quintIndex == 100000:
                    quintIndex = 5
                elif quintIndex == 1000000:
                    quintInterval = 20

                if quintIndex % quintInterval == 0:
                    quintFile.write( '{:12} {}\n'.format( quintIndex, prime - 12 ) )
        # check for the other kind of prime quintuplet
        elif ( prime - 23 ) % 30 == 0 and \
           diffs[ -1 ] == 4 and diffs[ -2 ] == 2 and diffs[ -3 ] == 4 and diffs[ -4 ] == 2:
            quintIndex += 1

            if quintIndex == 100000:
                quintIndex = 5
            elif quintIndex == 1000000:
                quintInterval = 20

            if quintIndex % quintInterval == 0:
                quintFile.write( '{:12} {}\n'.format( quintIndex, prime - 12 ) )

            # and we can catch prime sextuplets while we're at it
            if diffs[ -5 ] == 4:
                sextIndex += 1

                if sextIndex % sextInterval == 0:
                    sextFile.write( '{:12} {}\n'.format( sextIndex, prime - 16 ) )

    sexyQuadFile.close( )


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

