import math

count = 1
pcount = 0
target = 10001

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

while pcount < target:
    if is_prime(count):
        pcount += 1
        print ("prime number number", pcount)
        print (count)
    count += 1