#!/usr/bin/env python

import contextlib
import bz2
import pickle


def saveFile( var, fileName ):
    with contextlib.closing( bz2.BZ2File( fileName + '.pckl.bz2', 'wb' ) ) as pickleFile:
        pickle.dump( var, pickleFile )


def loadFile( fileName ):
    with contextlib.closing( bz2.BZ2File( fileName + 'pckl.bz2', 'rb' ) ) as pickleFile:
        return pickle.load( pickleFile )


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    lineCount = 1

    primesSize = 5

    primes = [ ]
    diffs = [ ]
    adiffs = [ ]

    for i in range( 0, primesSize ):
        primes.append( [ -9999999, -9999999 ] )

    for i in range( 0, primesSize - 1 ):
        diffs.append( 0 )
        adiffs.append( 0 )

    isolatedIndex = 0

    firstDataFile = 0
    lastDataFile = 9950

    numberOfTypes = 200

    isolatedIndex = [ 0 ] * numberOfTypes
    isolatedFile = [ ]

    for i in range( 0, numberOfTypes ):
        isolatedFile.append( open( 'c:\\data\primes\\isolated{:03}_primes.txt'.format( i * 2 + 4 ), 'w' ) )

    printInterval = 1000000

    for index, prime in readPrimeNumbers( firstDataFile, lastDataFile ):
        primes.append( [ index, prime ) ] )
        del primes[ 0 ]

        diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
        del diffs[ 0 ]

        sum = 0

        for i in range( 0, primesSize - 1 ):
            sum += diffs[ i ]
            adiffs[ i ] = sum

        if primes[ 0 ][ 0 ] % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        for i in range( 0, numberOfTypes ):
            diff = i * 2 + 4

            if diffs[ 0 ] > diff and diffs[ 1 ] > diff and isolatedIndex[ i ] <= 1000000:
                isolatedIndex[ i ] += 1
                isolatedFile[ i ].write( '{},{}\n'.format( isolatedIndex[ i ], primes[ 1 ][ 1 ] ) )

    for i in range( 0, numberOfTypes ):
        isolatedFile[ i ].close( )


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

