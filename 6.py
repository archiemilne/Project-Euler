x = 100 #input number
y = 0 #total of square of the sum (1 + 2)^2
z = 0 #total of the sum of the squares 1^2 + 2^2
a = 0 #root y

for i in range(1, x + 1):
    a = a + i
    z = z + (i * i)

y = a * a
print (y - z)