#!/usr/bin/env python  c`

import gmpy2
import os

from bitarray import bitarray

inputDirectory = "d:\\primes"
#outputDirectory = "c:\\sys\\ut\\rpn\\rpn"
outputDirectory = "d:\\primes"

primeFileIndex = 6


#//******************************************************************************
#//
#//  primes
#//
#//******************************************************************************

primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 ]


#//******************************************************************************
#//
#//  getPrimorial
#//
#//******************************************************************************

def getPrimorial( index ):
    result = 1

    for i in range( index ):
        result *= primes[ i ]

    return result


#//******************************************************************************
#//
#//  isRough
#//
#//******************************************************************************

def isRough( n, k ):
    for prime in primes:
        if prime >= k:
            return True

        if n % prime == 0:
            return False


#//******************************************************************************
#//
#//  generateDecodeArray
#//
#//******************************************************************************

def generateDecodeArray( index ):
    result = [ ]

    size = getPrimorial( index )
    base = primes[ index ] - 1

    for i in range( size ):
        if isRough( i + base, primes[ index ] ):
            result.append( i )

    return result


#//******************************************************************************
#//
#//  generateEncodeMap
#//
#//******************************************************************************

def generateEncodeMap( index ):
    result = { }

    size = getPrimorial( index )
    base = primes[ index ] - 1

    value = 0

    for i in range( size ):
        if isRough( i + base, primes[ index ] ):
            result[ i ] = value
            value += 1

    return result


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

def readPrimeNumbers( end=None ):
    bits = bitarray( )

    decodeArray = generateDecodeArray( primeFileIndex )

    base = primes[ primeFileIndex ] - 1
    chunkSize = len( decodeArray )
    baseChunkSize = getPrimorial( primeFileIndex )
    primeBase = base - baseChunkSize        # The very first time through will kick it up to base.

    if not end:
        end = 1000000000 # 40000000000

    for i in range( primeFileIndex ):
        yield i + 1, primes[ i ]

    primeIndex = primeFileIndex

    primesFile = open( inputDirectory + os.sep + 'primes.11.bin', 'rb' )

    quit = False

    while not quit:
        try:
            bits = bitarray( )
            bits.fromfile( primesFile, chunkSize * 100 )
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

                if primeIndex == end:
                    quit = True
                    break

        base += chunkSize

    primesFile.close( )

