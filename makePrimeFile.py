#!/usr/bin/env python

from bitarray import bitarray
import os

from primeDataUtils import generateEncodeMap, getPrimorial, outputDirectory, \
                           primeFileIndex, primes, readPrimeDataFiles

#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    firstDataFile = 0
    lastDataFile = 950

    printInterval = 100000

    encodeMap = generateEncodeMap( primeFileIndex )

    base = primes[ primeFileIndex ] - 1
    chunkSize = len( encodeMap )
    baseChunkSize = getPrimorial( primeFileIndex )
    marker = baseChunkSize + base

    #print( 'base', base )
    #print( 'chunkSize', chunkSize )
    #print( 'baseChunkSize', baseChunkSize )
    #print( 'marker', marker )

    primesFile = open( outputDirectory + os.sep + 'primes.bin', 'wb' )

    primeData = bitarray( chunkSize )
    primeData[ 0 : ] = False

    for index, prime in readPrimeDataFiles( firstDataFile, lastDataFile ):
        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        if prime < base:
            continue
        elif prime > marker:
            #print( primeData.to01( ), marker )
            primeData.tofile( primesFile )
            primeData[ 0 : ] = False

            while prime > marker:
                marker += baseChunkSize

        #print( 'offset', ( prime - base ) % baseChunkSize )
        #print( 'index', index, 'prime', prime, 'offset', encodeMap[ ( prime - base ) % baseChunkSize ] )
        primeData[ encodeMap[ ( prime - base ) % baseChunkSize ] ] = True

    primesFile.close( )


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

