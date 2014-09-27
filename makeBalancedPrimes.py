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

    inputList = [ 'c:\\data\\primes\\0000-0050.txt', 'c:\\data\\primes\\0050-0100.txt',
                  'c:\\data\\primes\\0100-0150.txt', 'c:\\data\\primes\\0150-0200.txt',
                  'c:\\data\\primes\\0200-0250.txt', 'c:\\data\\primes\\0250-0300.txt',
                  'c:\\data\\primes\\0300-0350.txt', 'c:\\data\\primes\\0350-0400.txt',
                  'c:\\data\\primes\\0400-0450.txt', 'c:\\data\\primes\\0450-0500.txt',
                  'c:\\data\\primes\\0500-0550.txt', 'c:\\data\\primes\\0550-0600.txt',
                  'c:\\data\\primes\\0600-0650.txt', 'c:\\data\\primes\\0650-0700.txt',
                  'c:\\data\\primes\\0700-0750.txt', 'c:\\data\\primes\\0750-0800.txt',
                  'c:\\data\\primes\\0800-0850.txt', 'c:\\data\\primes\\0850-0900.txt',
                  'c:\\data\\primes\\0900-0950.txt', 'c:\\data\\primes\\0950-1000.txt' ]

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

                    if primes[ center + 1 ][ 1 ] > 0:
                        balancedIndex[ i ] += 1
                        balancedFile[ i ].write( '{},{}\n'.format( balancedIndex[ i ], primes[ center + 1 ][ 1 ] ) )

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

