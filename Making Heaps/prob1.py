import random
from heap import *
import timeit

def prob1():
    global arr
    arr = []
    setupStr = 'from __main__ import prob1, make_heap, downheap, arr'
    print("n\tT(n)")
    for i in range (2, 21):
        arr.clear()
        for x in range (1, (5000 * i) + 1):
            arr.append(x)
        random.shuffle(arr)
        mytime = timeit.Timer('make_heap(arr)', setupStr)
        heapifyTime = mytime.timeit( 100 )
        print(str((i * 500)) + "\t" + str(heapifyTime))

if __name__ == "__main__":
    prob1()