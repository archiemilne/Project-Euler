import math

a = 0
b = 0
c = 0
run = True
target = 1000

while run:
    a += 1
    for i in range (1, a + 1):
        b = i
        c = math.sqrt((a * a)+(b * b))
        if (a + b + c) == target:
            print(a * b * c)
            run = False
