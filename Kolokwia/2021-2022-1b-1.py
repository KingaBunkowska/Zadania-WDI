import math


def is_prime(a):
    if a<2:
        return 0

    for i in range(2, int(math.sqrt(a)+1)):
        if a%i==0:
            return 0

    return 1


def product(T, i):
    result = 1
    for j in range(0, i):
        if is_prime(T[j]):
            result *= T[j]

    return result


def f(T, N):
    Max=None

    for i in range(N):
        if T[i] == product(T, i) and (Max == None or Max<T[i]):
            Max = T[i]

    return Max

N = 7
T = [2, 3, 5, 8, 30, 3, 90]

print(f(T, N))

