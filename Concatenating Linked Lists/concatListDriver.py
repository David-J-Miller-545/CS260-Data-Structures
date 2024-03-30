#!/usr/bin/env python3
# concatListDriver.py - Runs and times the functions from concatLists.py
#
# 1/22
#

from concatLists import *
import timeit


def prob1():
    print("Destructively Concatenating List A: " + cell.list2string(a.head) + "and List B: " + cell.list2string(b.head))
    print(cell.list2string(list_concat(a, b).head))
    print("Aftermath of List A: " + cell.list2string(a.head) + "\nAftermath of List B: " + cell.list2string(b.head))

def prob2():
    print("Constructively Concatenating List A: " + cell.list2string(a.head) + "and List B: " + cell.list2string(b.head))
    print(cell.list2string(list_concat_copy(a, b).head))
    print("Aftermath of List A: " + cell.list2string(a.head) + "\nAftermath of List B: " + cell.list2string(b.head))

def time():
    global l1, l2
    f = open("data.out", "w")
    setupStr = 'from concatListDriver import list_concat, list_concat_copy, l1, l2'
    for i in range (1, 16):
        l1 = generateListofSize(1000 * i)
        l2 = generateListofSize(1000 * i)

        mytime = timeit.Timer('list_concat(l1, l2)', setupStr)
        destructTime = mytime.timeit( 1 )
        mytime = timeit.Timer('list_concat_copy(l1, l2)', setupStr)
        constructTime = mytime.timeit( 1 )
        f.write(str(i * 1000) + ' ' + str(destructTime) + ' ' + str(constructTime) + '\n')
    f.close()
        
        
        