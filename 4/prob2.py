import sys

def fib2(n):
    c = len(memo) - 1
    if 0 <= n <= 1:
        memo[n] = n
        return n
    else: 
        for x in range(0, c):
            if memo[x] == None:
                break
            elif n == x:
                return memo[n]
        fibNum = fib2(n - 1) + fib2(n - 2)
        memo[n] = fibNum
        return fibNum



def prob2(n):
    global memo
    memo = [None] * 1000
    fibNum = fib2(n)
    memo.clear()
    return fibNum


if __name__ == "__main__":
    print(str(prob2(int(sys.argv[1]))))
