import math


def is_prime(a):
    a = int(a)
    if a<2:
        return 0

    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return 0

    return 1


def numbers(a, b, i=0, num = "", ai=0, bi=0):
    global t
    if ai == len(a) or bi == len(b):
        if ai == len(a):
            x = num + b[bi:]
        if bi == len(b):
            x = num + a[ai:]

        if is_prime(x) and x not in t:
                t.append(x)
                print(x)
                return is_prime(x)

        return 0

    return numbers(a, b, i+1, num + a[ai], ai+1, bi) + numbers(a, b, i+1, num + b[bi], ai, bi+1)




a = "111"
b = "17"
t = []
print(numbers(a, b))
