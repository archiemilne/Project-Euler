import math

big = 0

def rev(y):
    return int(y != 0) and ((y % 10) * \
             (10**int(math.log(y, 10))) + \
                          rev(y // 10))

for i in range (999, 0, -1):
    count = i
    while count > 0:
        x = count * i
        if x == rev(x) and x > big:
            big = x
        count -= 1

print big