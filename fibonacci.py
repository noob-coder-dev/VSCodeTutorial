def fib(n):
    if n <= 1: return n
    else: return fib(n-1) + fib(n-2)

var1 = fib(3)
var2 = fib(4)
print(fib(5))