import math


def iloczyn(a, sys):
    res = 1
    while a>0:
        res *= a%sys
        a //= sys

    return res


def is_prime(a):
    if a<2:
        return 0

    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return 0

    return 1


def size(a):
    i = 0
    while a>0:
        i+=1
        a//=10

    return i

def rotacja(a, x):
    for i in range(size(a)-1-x):
        x= a%10
        a//=10
        a += x * (10 **size(a))

    return a


def f(N):
    Max = 0
    for i in range(2, 17):
        for x in range(size(N)):
            a = rotacja(N, x)
            if is_prime(iloczyn(a, i)) and iloczyn(a, i)> Max:
                Max = a

    if Max==0:
        return None
    else:
        return Max

print(f(920))
