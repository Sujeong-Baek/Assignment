def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(1, 45):
    print("Fib(%d) = %d" % (i, fib(i)))



# Fib(0) -> 0
# Fib(1) -> 1
# Fib(n) = Fib(n-1) + Fib(n-2)

# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)
# fib(2) = fib(1) + fib(0)
