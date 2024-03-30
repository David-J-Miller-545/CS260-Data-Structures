from heap import *
from minheap import *

###NOT MY CODE###
def childNodes(i):
     return (2*i)+1, (2*i)+2

def traversed(a, i=0, d = 0):
    if i >= len(a):
        return 
    l, r =  childNodes(i)
    traversed(a, r, d = d+1)
    print("\t"*d + str(a[i]))
    traversed(a, l, d = d+1)
###NOT MY CODE###

if __name__ == "__main__":
    arr = [6, 14, 23, 20, 13, 31, 25, 68, 147, 3646, 1, 27]
    arrd = [6, 2, 8, 21, 67, 435, 98, 223, 49, 60, 42, 55, 93, 111, 23, 12, 15, 27]

    print(str(arr))
    traversed(arr)
    make_heap(arr)
    print(str(arr))
    traversed(arr)
    
    print(str(arr))
    traversed(arr)
    minmake_heap(arr)
    print(str(arr))
    traversed(arr)
        