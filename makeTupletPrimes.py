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

    primes = [ -1 ] * 8  # otherwise it thinks 0 and 2 are twin primes
    diffs = [ 0 ] * 7

    twinIndex = 0
    tripletIndex = 0
    quadIndex = 0
    quintIndex = 0
    sextIndex = 0

    twinInterval = 1
    tripletInterval = 1
    quadInterval = 1
    quintInterval = 1
    sextInterval = 1

    printInterval = 100000

    print( )

    twinFile = open( outputDirectory + os.sep + 'twin_primes.txt', 'w' )
    tripletFile = open( outputDirectory + os.sep + 'triplet_primes.txt', 'w' )
    quadFile = open( outputDirectory + os.sep + 'quad_primes.txt', 'w' )
    quintFile = open( outputDirectory + os.sep + 'quint_primes.txt', 'w' )
    sextFile = open( outputDirectory + os.sep + 'sext_primes.txt', 'w' )

    quadIndex += 1
    quadFile.write( '{:12} {}\n'.format( 1, 5 ) )

    quintIndex += 1
    quintFile.write( '{:12} {}\n'.format( 1, 5 ) )

    for index, prime in readPrimeNumbers( 10000000000 ):
        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        primes.append( prime )
        del primes[ 0 ]

        diffs.append( primes[ -1 ] - primes[ -2 ] )
        del diffs[ 0 ]

        # first check for twin primes
        if diffs[ -1 ] == 2:
            twinIndex += 1
            twinInterval = updateOutputInterval( twinIndex, twinInterval )

            if twinIndex % twinInterval == 0:
                twinFile.write( '{:12} {}\n'.format( twinIndex, prime - 2 ) )

        # them check for a triplet
        if ( diffs[ -1 ] == 2 and diffs[ -2 ] == 4 ) or \
           ( diffs[ -1 ] == 4 and diffs[ -2 ] == 2 ):
            tripletIndex += 1

            if tripletIndex % tripletInterval == 0:
                tripletInterval = updateOutputInterval( tripletIndex, tripletInterval )
                tripletFile.write( '{:12} {}\n'.format( tripletIndex, prime - 6 ) )

        # next, check for a quadruplet
        if ( prime - 19 ) % 30 == 0 and \
           diffs[ -1 ] == 2 and diffs[ -2 ] == 4 and diffs[ -3 ] == 2:
            quadIndex += 1

            if quadIndex % quadInterval == 0:
                quadInterval = updateOutputInterval( quadIndex, quadInterval, 1 )
                quadFile.write( '{:12} {}\n'.format( quadIndex, prime - 8 ) )

            if diffs[ -4 ] == 4:
                quintIndex += 1

                if quintIndex % quintInterval == 0:
                    quintInterval = updateOutputInterval( quintIndex, quintInterval )
                    quintFile.write( '{:12} {}\n'.format( quintIndex, prime - 12 ) )
        # check for the other kind of prime quintuplet
        elif ( prime - 23 ) % 30 == 0 and \
           diffs[ -1 ] == 4 and diffs[ -2 ] == 2 and diffs[ -3 ] == 4 and diffs[ -4 ] == 2:
            quintIndex += 1

            if quintIndex % quintInterval == 0:
                quintInterval = updateOutputInterval( quintIndex, quintInterval, 2 )
                quintFile.write( '{:12} {}\n'.format( quintIndex, prime - 12 ) )

            # and we can catch prime sextuplets while we're at it
            if diffs[ -5 ] == 4:
                sextIndex += 1

                # These are rare enough that we'll save every single one.
                if sextIndex % sextInterval == 0:
                    sextFile.write( '{:12} {}\n'.format( sextIndex, prime - 16 ) )

    twinFile.close( )
    tripletFile.close( )
    quadFile.close( )
    quintFile.close( )
    sextFile.close( )


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

