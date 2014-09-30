#!/usr/bin/env python

#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
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

    diffsFile = open( 'c:\\data\primes\\prime_diffs-0000-0050.txt', 'w' )

    previousPrime = -9999999
    printInterval = 10000000

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
                    print( '{:,}'.format( index ) )

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

