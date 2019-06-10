#!/usr/bin/env python

import gmpy2
import os

from bitarray import bitarray

inputDirectory = "c:\\rick\\primes"
outputDirectory = "c:\\rick\\primes"

primeFileIndex = 7


#//******************************************************************************
#//
#//  primes
#//
#//******************************************************************************

primeNumbers = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 ]


#//******************************************************************************
#//
#//  getPrimorial
#//
#//******************************************************************************

def getPrimorial( index ):
    result = 1

    for i in range( index ):
        result *= primeNumbers[ i ]

    return result


#//******************************************************************************
#//
#//  isRough
#//
#//******************************************************************************

def isRough( n, k ):
    for prime in primeNumbers:
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
    base = primeNumbers[ index ] - 1

    for i in range( size ):
        if isRough( i + base, primeNumbers[ index ] ):
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
    base = primeNumbers[ index ] - 1

    value = 0

    for i in range( size ):
        if isRough( i + base, primeNumbers[ index ] ):
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
#//  readPrimeDataFiles
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
#//  updateOutputInterval
#//
#//  The idnex should always be divisible by the interval.
#//
#//******************************************************************************

def updateOutputInterval( index, outputInterval, rarity=0 ):
    if rarity == 0:
        if index == 100:
            return 5
        elif index == 1000:
            return 10
        elif index == 10000:
            return 50
        elif index == 100000:
            return 200
        elif index == 1000000:
            return 500
        elif index == 10000000:
            return 1000
        elif index == 100000000:
            return 4000
        elif index == 1000000000:
            return 10000
        elif index == 10000000000:
            return 50000
    elif rarity == 1:
        if index == 1000:
            return 5
        elif index == 10000:
            return 10
        elif index == 100000:
            return 50
        elif index == 1000000:
            return 200
        elif index == 10000000:
            return 500
        elif index == 100000000:
            return 1000
        elif index == 1000000000:
            return 4000
        elif index == 10000000000:
            return 10000
        elif index == 100000000000:
            return 50000
    elif rarity == 2:
        if index == 10000:
            return 5
        elif index == 100000:
            return 10
        elif index == 1000000:
            return 50
        elif index == 10000000:
            return 200
        elif index == 100000000:
            return 500
        elif index == 1000000000:
            return 1000
        elif index == 10000000000:
            return 4000
        elif index == 100000000000:
            return 10000
        elif index == 1000000000000:
            return 50000
    elif rarity >= 3:
        return 1

    return outputInterval


#//******************************************************************************
#//
#//  readPrimeNumbers
#//
#//******************************************************************************

def readPrimeNumbers( end=None ):
    bits = bitarray( )

    decodeArray = generateDecodeArray( primeFileIndex )

    base = primeNumbers[ primeFileIndex ] - 1
    chunkSize = len( decodeArray )
    baseChunkSize = getPrimorial( primeFileIndex )
    primeBase = base - baseChunkSize        # The very first time through will kick it up to base.

    if not end:
        end = 1000000000 # 40000000000

    for i in range( primeFileIndex ):
        yield i + 1, primeNumbers[ i ]
        #print( i + 1, primeNumbers[ i ] )

    primeIndex = primeFileIndex

    primesFile = open( inputDirectory + os.sep + 'primes.bin', 'rb' )

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
                #print( primeIndex, prime )

                if primeIndex == end:
                    quit = True
                    break

        base += chunkSize

    primesFile.close( )

