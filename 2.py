total = 0
fib = 0
a = 0
b = 1

while fib < 3524578: #highest even number before 4 mil because jank code
    fib = a + b
    a = b
    b = fib

    if (fib % 2) == 0:
        total += b

print total