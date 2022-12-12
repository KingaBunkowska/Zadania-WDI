import math

def sieve_of_erastosthenes(a):
    t = [1 for _ in range(a)]
    t[0] = t[1] = 0
    for i in range(2, a):
        if t[i]:
            for j in range(i * i, a, i):
                t[j] = 0

    return t


def prime_factors(a):
    if a <2:
        return 0

    res = [0 for _ in range(20)]
    cur_i = 0
    tmp = int(math.sqrt(a)) + 1
    sieve = sieve_of_erastosthenes(tmp)

    while a>1:
        for i in range(tmp):
            while sieve[i] and a%i==0:
                if cur_i == 0 or res[cur_i - 1] != i:
                    res[cur_i] = i
                    cur_i += 1

                a //= i

    return res


def sum_factors(t, i=0, product = 1):
    if i >= len(t) or t[i] == 0:
        if product == 1:
            return 0

        return product

    return sum_factors(t, i+1, product) + sum_factors(t, i+1, product * t[i])


a = 60
print(sum_factors(prime_factors(a)))