import math


def is_prime(a):
    if a<2:
        return 0

    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return 0

    return 1


def int_len(a):
    res = 0
    while a!= 0:
        res += 1
        a //= 10

    return res


def to_dec(a):
    res = 0

    for i in range(0, int_len(a)):
        res += a%10 * (2 ** i)
        a //= 10

    return res


def to_number(beg, end):
    res = 0
    for i in range(beg, end+1):
        res *= 10
        res += t[i]

    return res


def parting(index):
    global flag
    if index == len(t) or flag == 1:
        flag = 1
    else:
        for size in range(2, min(30, len(t)-index+1)):
            if size != len(t):
                if not flag and is_prime(to_dec(to_number(index, index + size - 1))):
                    parting(index + size)

    if not flag:
        return 0
    else:
        return 1


t = [1, 1, 0, 1, 0, 0]
flag = 0

print(parting(0))
