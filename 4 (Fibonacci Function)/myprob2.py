import sys

def fib2(n):
    c = len(memo)
    if n < c:
        return memo[n]
    else: 
        fibNum = fib2(n - 1) + fib2(n - 2)
        memo.append(fibNum)
        return fibNum



def prob2(n):
    global memo
    memo = [0, 1]
    fibNum = fib2(n)
    memo.clear()
    return fibNum


if __name__ == "__main__":
    print(str(prob2(int(sys.argv[1]))))
