import math

def is_perfect_sq(x):
    s=int(math.sqrt(x))
    return s*s==x

def is_fibonaci(n):
    return is_perfect_sq(5*n*n + 4) or is_perfect_sq(5*n*n-4)

num =465

if is_fibonaci(num):
    print("fib")

else:
    print("no fibonacci")