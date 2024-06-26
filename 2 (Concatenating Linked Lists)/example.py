#!/usr/bin/env python3
# example.py - an example of "including" (importing) a user-defined type,
#		and of using the timeit function
#
# 1/07
#
# THIS FILE WAS PROVIDED FOR THIS ASSIGNMENT BY KURT SCHMIDT
# NOT MADE BY DAVID MILLER

import random
import timeit

import cell
import myfile
import concatLists

print( str(concatLists.a) )

def bar( n ):
	for i in range( 1, n ) :
		i*2

#######   MODULES   ##########################

	# We can refer to stuff in another module simply by qualifying it:
c = cell.Cell( 24 )
myfile.foo( 5 )
print( '' )

	# Or, instead of importing an entire module, we can choose single
	# functions/classes/etc, and add them to the local namespace:

from myfile import foo
foo( 3 )
print( '' )


########  TIMING   #########################################

	#### Okay, if the function is local to this file, defined here, then
	# set-up
c = 1000000
mytime = timeit.Timer( 'bar(c)', 'from __main__ import bar, c' )
	# actually time a single call to bar
delta = mytime.timeit( 1 )
print( "1 run of bar( 1000000 ) took: " + str( delta ) + " seconds." )
#delta = mytime.timeit( 5 )
#print "5 runs of bar( 1000000 ) took: " + str( delta ) + " seconds."
print( '' )

	#### If the function is in another file, do it like this:
	# set-up
mytime = timeit.Timer( 'bar(1000000)', 'from myfile import bar' )
	# actually time a single call to foo
delta = mytime.timeit( 1 )
print( "1 run of foo( 1000000 ) took: " + str( delta ) + " seconds." )
#delta = mytime.timeit( 5 )
#print "5 runs of foo( 1000000 ) took: " + str( delta ) + " seconds."
print( '' )

setupStr = 'from myfile import list_concat'
setupStr += '; import concatLists'
mytime = timeit.Timer( 'list_concat( concatLists.a, concatLists.b)', setupStr )
print( 'calling list_concat from cell.py on a, b, from foo.py:' )
delta = mytime.timeit( 5 )
print( "1 run of list_concat( a, b ) took: " + str( delta ) + " seconds." )

