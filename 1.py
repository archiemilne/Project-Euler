total = 0
for x in range (3,1000,3):
    total += x
    print x
for x in range (5,1000,5):
    if (x % 3) != 0:
        total += x
        print x


print total