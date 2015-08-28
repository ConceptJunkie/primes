#!/usr/bin/env python

#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    lineCount = 1

    firstDataFile = 6000
    lastDataFile = 10000

    previousPrime = -9999999

    inputList = [ ]

    diffsFile = open( 'c:\\data\primes\\prime_diffs-6900-6950.txt', 'w' )
    printInterval = 10000

    print( )

    current = firstDataFile

    while current <= lastDataFile:
        inputList.append( 'c:\\data\primes\\{:04}-{:04}.txt'.format( current, current + 50 ) )
        current += 50

    for fileName in inputList:
        with open( fileName, 'r' ) as file:
            for line in file:
                items = line[ : -1 ].split( ',' )

                if previousPrime == -9999999:
                    previousPrime = int( items[ 1 ] )
                    continue

                index = int( items[ 0 ] )
                prime = int( items[ 1 ] )

                diffsFile.write( '{},{}\n'.format( index - 1, prime - previousPrime ) )

                previousPrime = prime

                if index % printInterval == 0:
                    print( '\r{:,}'.format( index ), end='' )

                if index % 50000000 == 1:
                    diffsFile.close( )

                    fileNum = index // 1000000

                    diffsFile = open( 'c:\\data\primes\\prime_diffs-{:04}-{:04}.txt'.format( fileNum, fileNum + 50 ), 'w' )

    diffsFile.close( )


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

