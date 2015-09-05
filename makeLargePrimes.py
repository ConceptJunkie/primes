#!/usr/bin/env python

#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    lineCount = 1

    firstDataFile = 1000
    lastDataFile = 12000

    previousPrime = -9999999

    inputList = [ ]

    largeFile = open( 'c:\\data\primes\\large_primes.txt', 'w' )
    printInterval = 10000

    print( )

    current = firstDataFile

    while current <= lastDataFile:
        inputList.append( 'c:\\data\primes\\{:05}-{:05}.txt'.format( current, current + 50 ) )
        current += 50

    for fileName in inputList:
        with open( fileName, 'r' ) as file:
            for line in file:
                items = line[ : -1 ].split( ',' )

                index = int( items[ 0 ] )
                prime = int( items[ 1 ] )

                if index % 1000 == 0:
                    diffsFile.write( '{},{}\n'.format( index, prime ) )

                if index % printInterval == 0:
                    print( '\r{:,}'.format( index ), end='' )

    largeFile.close( )


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

