#!/usr/bin/env python3
# stack - the node class is a specific linked list given some functionality by the also produced stack class
# 
# 1/30

class Node:

	def __init__( self, data, next=None ):
		self.data = data
		self.next = next

	def __str__( self ):
		return str( self.data )

	def echo( self ):
		print( self.__str__() )

class Stack:
    def __init__(self):
        self.top = None
    
    def pop(self):
        if not self.isEmpty():
            popped = self.top
            self.top = self.top.next
            return popped.data
        else:
            return None

    def peek(self):
        return self.top.data

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node