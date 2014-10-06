#!/usr/bin/env python

#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    lineCount = 1

    primesSize = 11
    center = primesSize // 2 - 1

    primes = [ ]
    diffs = [ ]

    for i in range( 0, primesSize ):
        primes.append( [ -9999999, -9999999 ] )

    for i in range( 0, primesSize - 1 ):
        diffs.append( 0 )

    firstDataFile = 0
    lastDataFile = 7450

    inputList = [ ]

    current = firstDataFile

    while current <= lastDataFile:
        inputList.append( 'c:\\data\primes\\{:04}-{:04}.txt'.format( current, current + 50 ) )
        current += 50

    numberOfTypes = 5

    balancedIndex = [ 0 ] * numberOfTypes
    balancedFile = [ ]

    for i in range( 0, numberOfTypes ):
        balancedFile.append( open( 'c:\\data\primes\\balanced{:02}_primes.txt'.format( i + 1 ), 'w' ) )

    printInterval = 100000

    for fileName in inputList:
        with open( fileName, 'r' ) as file:
            for line in file:
                items = line[ : -1 ].split( ',' )

                primes.append( [ int( items[ 0 ] ), int( items[ 1 ] ) ] )
                del primes[ 0 ]

                diffs.append( primes[ -1 ][ 1 ] - primes[ -2 ][ 1 ] )
                del diffs[ 0 ]

                sum = 0

                if primes[ 0 ][ 0 ] % printInterval == 0:
                    print( 'balanced: {:,}'.format( primes[ 0 ][ 0 ] ) )

                for i in range( 0, numberOfTypes ):
                    skip = False

                    for j in range( 0, i + 1 ):
                        if ( diffs[ center - j ] != diffs[ center + j + 1 ] ):
                            skip = True
                            break

                    if skip:
                        continue

                    if primes[ center - i ][ 1 ] > 0:
                        balancedIndex[ i ] += 1
                        balancedFile[ i ].write( '{},{}\n'.format( balancedIndex[ i ], primes[ center - i ][ 1 ] ) )

    for i in range( 0, numberOfTypes ):
        balancedFile[ i ].close( )


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

