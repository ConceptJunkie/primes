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

    with contextlib.closing( bz2.BZ2File( inFileName, 'rb' ) ) as pickleFile:
        data = pickle.load( pickleFile )

    for i in data:
        print( i, data[ i ] )


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

