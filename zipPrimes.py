#!/usr/bin/env python

import sys


#//******************************************************************************
#//
#//  main
#//
#//******************************************************************************

def main( ):
    for i in range( 1000 ):
        print( 'zip {:05}-{:05}.zip {:05}-{:05}.txt'.format( i * 50, i * 50 + 50, i * 50, i * 50 + 50 ) )


#//******************************************************************************
#//
#//  __main__
#//
#//******************************************************************************

if __name__ == '__main__':
    main( )

