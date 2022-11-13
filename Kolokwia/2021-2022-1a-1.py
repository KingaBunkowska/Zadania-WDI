import math

def size(liczba):
    result = 0
    while liczba>0:
        result += 1
        liczba//=10

    return result

def obciecie(M, N, liczba):
    liczba = liczba//(10**N)
    result = 0
    len = size(liczba)
    for i in range(len - M):
        result += (liczba%10) * 10**i
        liczba //= 10

    return result


def is_prime(a):
    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return 0

    return 1

def diffrent_digits(a):
    T = [0 for _ in range(10)]
    while a>0:
        x = a%10
        T[x] += 1
        a //= 10
        if T[x]>1:
            return 0

    return 1

def f(a):
    Max = 0
    for m in range(size(a)):
        for n in range(size(a)):
            x = obciecie(m, n, a)
            if x!=0 and diffrent_digits(x) and is_prime(x) and x>Max:
                Max = x

    return Max


print(f(1202742516))


