import sys
import timeit
from prob1 import *
from prob2 import *



def prob3():
    global n 
    f = open("1.out", "w")
    setupStr = 'from __main__ import prob1, n'
    for i in range (1, 9):
        n = 5 * i
        mytime = timeit.Timer('prob1(n)', setupStr)
        fibTime = mytime.timeit( 1 )
        f.write(str(n) + ' ' + str(fibTime) + '\n')
    f.close()
    f2 = open("2.out", "w")
    setupStr = 'from __main__ import prob2, n'
    for i in range (1, 12):
        n = 400 + 50 * i
        mytime = timeit.Timer('prob2(n)', setupStr)
        fibTime = mytime.timeit( 1000 )
        f2.write(str(n) + ' ' + str(fibTime) + '\n')
    f2.close()

if __name__ == "__main__":
    prob3()
