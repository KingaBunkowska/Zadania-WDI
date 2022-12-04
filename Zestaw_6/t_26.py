import math


def to_dec(a):
    res = 0
    i = 0
    while a!=0:
        res += a%10 * (2**i)
        a //= 10
        i += 1

    return res


def is_prime(a):
    if a<2:
        return 0

    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return 0

    return 1


def make_binary (a, b, cur = "1"):
    if a == 0 or b == 0:
        if a == 0:
            cur = cur + "0" * b
        if b == 0:
            cur = cur + "1" * a

        if is_prime(to_dec(int(cur))) == 0:
            print(cur)
            return 1

        return 0

    return make_binary(a-1, b, cur + "1") + make_binary(a, b-1, cur + "0")


a = 2
b = 3
print(make_binary(a-1, b))