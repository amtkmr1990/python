

def generator_prime(r):
    for a in range(2, r + 1):
        k = 0
        for i in range(2, a // 2 + 1):
            if a % i == 0 :
                k = k + 1
        if k <= 0:
            yield a


g = generator_prime(2)
print(next(g))