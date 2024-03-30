#!/usr/bin/env python3
# Cell - module for a "cons" cell - a node in a linked list - And added a "list" class to keep the head 
#	     and tail of a list known
# 
# 1/22
#
#

import sys

class Cell:
	"""Just a little wrapper for a cons cell, a node in a singly-linked list,
	essentially, a 2-tuple:
		1. the data (the payload, the reason for existing)
		2. the rest of the list

	No operations are provided
	"""

	def __init__( self, data, next=None ):
		self.data = data
		self.next = next

	def __str__( self ):
		return str( self.data )

	def echo( self ):
		print( self.__str__() )

class List:

	def __init__(self, head, tail=None):
		self.head = head
		if tail == None:
			self.tail = head
		else:
			self.tail = tail
		self.next = head.next
		self.data = head.data
    
	def add (self, data):
		self.tail.next = Cell(data)
		self.tail = self.tail.next


def list2string( L ) :
	
	if L is None :
		rv = '()'
	else :
		rv = '('
		while L.next is not None :
			rv += L.__str__() + ','
			L = L.next
		rv += L.__str__() + ')'

	return rv

def main( argv=sys.argv ) :
	"Just a test driver - NOT part of the class"

	c = Cell( 13 )
	print( "c is holding: " + list2string( c ))
	d = Cell( 12, c )
	print(  "d is holding: " + list2string( d ))

if __name__ == "__main__" :
	# then this was NOT included in another file, so, run the test driver
	main()

