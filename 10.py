import math

sum = 0
target = 2000000

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

for i in range(1, target):
    if is_prime(i):
        sum += i

print (sum)