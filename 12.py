#very very slow / need to make more eff

x = []
count = 1
tri = 0

while len(x) <= 500:
    x = []
    tri += count
    for i in range(1, tri+1):
        if(tri%i == 0):
            x.append(i)
    count += 1
    print (len(x))

print (tri)