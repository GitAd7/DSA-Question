def fib(n):
    if n<=1: # Base case
        return n
    return fib(n-1) + fib(n-2)