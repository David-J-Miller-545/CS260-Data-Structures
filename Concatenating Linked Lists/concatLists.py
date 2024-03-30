#!/usr/bin/env python3
# concatLists.py - includes some list functionality, but most importantly contains functions
#		           that destructively and constructively concatentate lists together
#
# 1/22
#

import cell
from cell import Cell, List

a = List(Cell('a'))
a.add('b')
a.add('c')

b = List(Cell(11))
b.add(12)
b.add(13)

def generateListofSize(x):
    L = List(Cell('1'))
    for i in range (2, x + 1):
        L.add(i)
    return L

# MAIN FUNCTIONS #
def list_concat(A, B):
    A.tail.next = B.head
    return A

def list_concat_copy(A, B):
    L = list_copy(A)
    L.tail.next = list_copy(B).head
    
    return L

def list_copy(A):
    i = A.head
    L = List(Cell(i.data))
    
    while i.next != None:
        L.add(i.next.data)
        i = i.next
    
    return L
#                #


if __name__ == "__main__":
    print("List A: " + cell.list2string(a.head))
    print("List B: " + cell.list2string(b.head))
    print("\nConcatenated Copies:")
    print(cell.list2string(list_concat_copy(a, b).head))
    print("List A: " + cell.list2string(a.head))
    print("List B: " + cell.list2string(b.head))

    print("\nDestructive: ")
    print(cell.list2string(list_concat(a, b).head))
    print("List A: " + cell.list2string(a.head))
    print("List B: " + cell.list2string(b.head))

    print("\nGenerated List: ")
    print(cell.list2string(generateListofSize(25).head))