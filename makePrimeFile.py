#!/usr/bin/env python

from bitarray import bitarray
import os

from primeDataUtils import outputDirectory, readPrimeDataFiles

offsetArray = {
     1   : 0,       3   : 1,        7   : 2,        9   : 3,        13  : 4,
     19  : 5,       21  : 6,        27  : 7,        31  : 8,        33  : 9,
     37  : 10,      43  : 11,       49  : 12,       51  : 13,       57  : 14,
     61  : 15,      63  : 16,       69  : 17,       73  : 18,       79  : 19,
     87  : 20,      91  : 21,       93  : 22,       97  : 23,       99  : 24,
     103 : 25,      111 : 26,       117 : 27,       121 : 28,       127 : 29,
     129 : 30,      133 : 31,       139 : 32,       141 : 33,       147 : 34,
     153 : 35,      157 : 36,       159 : 37,       163 : 38,       169 : 39,
     171 : 40,      177 : 41,       181 : 42,       183 : 43,       187 : 44,
     189 : 45,      199 : 46,       201 : 47,
}


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    firstDataFile = 0
    lastDataFile = 39950

    outputInterval = 100
    printInterval = 100000

    print( )

    chunkSize = 210

    marker = chunkSize + 10

    primesFile = open( 'primes.bin', 'wb' )

    primeData = bitarray( 48 )
    primeData[ 0 : ] = False

    for index, prime in readPrimeDataFiles( firstDataFile, lastDataFile ):
        if index % printInterval == 0:
            print( '\r{:,}'.format( index ), end='' )

        if prime < 10:
            continue
        elif prime > marker:
            #print( primeData.to01( ), marker )
            primeData.tofile( primesFile )
            primeData[ 0 : ] = False

            while prime > marker:
                marker += chunkSize

        #print( 'index', index, 'prime', prime, 'offset', offsetArray[ ( prime - 10 ) % chunkSize ] )
        primeData[ offsetArray[ ( prime - 10 ) % chunkSize ] ] = True

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


