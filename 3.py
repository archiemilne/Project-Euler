
victim = 600851475143
prime_factors = set()

if victim % 2 == 0:
    prime_factors.add(2)
while victim % 2 == 0:
    victim = victim // 2
    if victim == 1:
        print prime_factors
for factor in range(3, victim + 1, 2):
    if victim % factor == 0:
        prime_factors.add(factor)
        while victim % factor == 0:
            victim = victim // factor
            if victim == 1:
                print prime_factors