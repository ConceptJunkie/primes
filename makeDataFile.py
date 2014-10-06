#!/usr/bin/env python

import bz2
import contextlib
import pickle
import sys


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    inFileName = sys.argv[ 1 ]
    outFileName = sys.argv[ 2 ]

    interval = int( sys.argv[ 3 ] )

    if len( sys.argv ) >= 6:
        threshold = int( sys.argv[ 4 ] )
        newInterval = int( sys.argv[ 5 ] )
    else:
        threshold = 0
        newInterval = 0

    if len( sys.argv ) >= 8:
        threshold2 = int( sys.argv[ 4 ] )
        newInterval2 = int( sys.argv[ 5 ] )
    else:
        threshold2 = 0
        newInterval2 = 0

    printInterval = 100000

    data = { }

    count = 0

    with open( inFileName, 'r' ) as file:
        for line in file:
            items = line[ : -1 ].split( ',' )
            key = int( items[ 0 ] )
            value = int( items[ 1 ] )

            if ( key == 1 ) or ( key % interval == 0 ):
                data[ key ] = value

            count += 1

            if count % printInterval == 0:
                print( count )

            if ( threshold > 0 ) and ( key >= threshold ):
                interval = newInterval
                threshold = 0

            if ( threshold2 > 0 ) and ( key >= threshold2 ):
                interval = newInterval2
                threshold2 = 0

    with contextlib.closing( bz2.BZ2File( outFileName + '.pckl.bz2', 'wb' ) ) as pickleFile:
        pickle.dump( data, pickleFile )


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

