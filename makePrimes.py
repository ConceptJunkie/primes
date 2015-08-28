#!/usr/bin/env python

import concurrent.futures
import pyprimes
import sys


#//******************************************************************************
#//
#//  isPrime
#//
#//******************************************************************************

def isPrime( arg ):
    return pyprimes.isprime( arg )


# //******************************************************************************
# //
# //  getNextPrimeCandidate
# //
# //  p is the next prime candidate.  Starting with ( p - 10 ) mod 30, we only
# //  need to check 8 values out of the next 30, which eliminates all multiples
# //  of 2, 3 and 5, and saves us a lot of unnecessary checking.
# //
# //  We only need to check for a prime if ( p - 10 ) mod 30 is 1, 3, 7, 9, 13, 19,
# //  21 or 27.
# //
# //******************************************************************************

def getNextPrimeCandidate( p ):
    f = ( p - 10 ) % 30

    moduloTable = {
        0 : 1,
        1 : 2,
        2 : 1,
        3 : 4,
        4 : 3,
        5 : 2,
        6 : 1,
        7 : 2,
        8 : 1,
        9 : 4,
        10 : 3,
        11 : 2,
        12 : 1,
        13 : 6,
        14 : 5,
        15 : 4,
        16 : 3,
        17 : 2,
        18 : 1,
        19 : 2,
        20 : 1,
        21 : 6,
        22 : 5,
        23 : 4,
        24 : 3,
        25 : 2,
        26 : 1,
        27 : 4,
        28 : 3,
        29 : 2
    }

    return p + moduloTable[ f ]


#//******************************************************************************
#//
#//  makePrimeBatch
#//
#//******************************************************************************

batchSize = 100000

def makePrimeBatch( start ):
    p = getNextPrimeCandidate( start )
    stop = start + batchSize

    primes = [ ]

    while p <= stop:
        if isPrime( p ):
            primes.append( p )

        p = getNextPrimeCandidate( p )

    return primes


#//******************************************************************************
#//
#//  makePrimes
#//
#//******************************************************************************

def makePrimes( index, prime, count ):
    fileName = '{:05}-{:05}.txt'.format( index // 1000000, index // 1000000 + 50 )
    file = open( fileName, "w" )

    p = prime
    n = index

    while True:
        primes = [ ]

        with concurrent.futures.ProcessPoolExecutor( ) as executor:
            for batch in executor.map( makePrimeBatch, range( p, p + batchSize * 100, batchSize ) ):
                primes.extend( batch )

        finished = sorted( primes )

        for p in finished:
            n += 1
            file.write( '{},{}\n'.format( n, p ) )

            if n == index + count:
                print( '\r{:,}'.format( n ), end='' )
                file.close( )
                return n, p

        print( '\r{:,} - {:,}'.format( n, p ), end='' )

        p = finished[ -1 ]


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    index = sys.argv[ 1 ]
    index = ''.join( [ i for i in index if i not in ',' ] )
    index = int( index )

    prime = sys.argv[ 2 ]
    prime = ''.join( [ i for i in prime if i not in ',' ] )
    prime = int( prime )

    print( )

    while True:
        index, prime = makePrimes( index, prime, 50000000 )


#//******************************************************************************
#//
#//  __main__
#//
#//******************************************************************************

if __name__ == '__main__':
    main( )

