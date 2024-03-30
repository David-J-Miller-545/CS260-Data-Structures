import sys

def fib(n):
    if 0 <= n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def prob1(n):
    return(fib(n))

if __name__ == "__main__":
    print(str(prob1(int(sys.argv[1]))))