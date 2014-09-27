#!/usr/bin/env python

import pyprimes
import sys


#//******************************************************************************
#//
#//  isPrime
#//
#//******************************************************************************

def isPrime( arg ):
    return pyprimes.isprime( int( arg ) )


#//******************************************************************************
#//
#//  getNextPrimeCandidate
#//
#//******************************************************************************

def getNextPrimeCandidate( p, f ):
    if f == 1:
        p += 2
        f = 3
    elif f == 3:
        p += 4
        f = 7
    elif f == 7:
        p += 2
        f = 9
    else:
        p += 2
        f = 1

    return p, f


#//******************************************************************************
#//
#//  makePrimes
#//
#//******************************************************************************

def makePrimes( n, p ):
    f = p % 10

    fileName = str( n // 1000000 ) + '-' + str( n // 1000000 + 50 ) + '.txt'
    file = open( fileName, "w" )

    while True:
        p, f = getNextPrimeCandidate( p, f )

        if isPrime( p ):
            n += 1
            file.write( '{},{}\n'.format( n, p ) )

            if n % 1000000 == 0:
                print( '{:,}'.format( n ) )

            if n % 50000000 == 0:
                file.close( )
                return


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

    makePrimes( index, prime )


#//******************************************************************************
#//
#//  __main__
#//
#//******************************************************************************

if __name__ == '__main__':
    main( )

