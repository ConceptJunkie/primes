#!/usr/bin/env python

import gmpy2
import os

from bitarray import bitarray

inputDirectory = "f:\\primes"
#outputDirectory = "c:\\sys\\ut\\rpn\\rpn"
outputDirectory = "d:\\dev\\github\\primes"


#//******************************************************************************
#//
#//  isPrime
#//
#//******************************************************************************

def isPrime( n ):
    return True if gmpy2.is_bpsw_prp( n ) else False


#//******************************************************************************
#//
#//  readPrimeNumbers
#//
#//******************************************************************************

def readPrimeDataFiles( firstDataFile, lastDataFile ):
    inputList = [ ]

    current = firstDataFile

    while current <= lastDataFile:
        inputList.append( inputDirectory + os.sep + '{:05}-{:05}.txt'.format( current, current + 50 ) )
        current += 50

    for fileName in inputList:
        with open( fileName, 'r' ) as file:
            for line in file:
                items = line[ : -1 ].split( ',' )

                yield int( items[ 0 ] ), int( items[ 1 ] )


#//******************************************************************************
#//
#//  readPrimeNumbers
#//
#//******************************************************************************

def readPrimeNumbers( ):
    decodeArray = [ 1, 3, 7, 9, 13, 19, 21, 27, 31, 33, 37, 43, 49, 51, 57, 61, 63, 69,
                    73, 79, 87, 91, 93, 97, 99, 103, 111, 117, 121, 127, 129, 133, 139,
                    141, 147, 153, 157, 159, 163, 169, 171, 177, 181, 183, 187, 189,
                    199, 201 ]

    bits = bitarray( )

    primeIndex = 4
    base = 10
    chunkSize = 48
    baseChunkSize = 210
    primeBase = -200       # The very first time through will kick it up to 10.

    yield 1, 2
    yield 2, 3
    yield 3, 5
    yield 4, 7

    primesFile = open( 'primes.bin', 'rb' )

    while True:
        try:
            bits = bitarray( )
            bits.fromfile( primesFile, 48000 )
        except:
            break

        for index, bit in enumerate( bits ):
            #print( 'index', index, 'bit', bit )

            if index % chunkSize == 0:
                primeBase += baseChunkSize

            if bit:
                prime = primeBase + decodeArray[ index % chunkSize ]
                primeIndex += 1
                yield primeIndex, prime

        base += chunkSize

    primesFile.close( )

