import math


def is_prime(a):
    if a<2:
        return 0

    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return 0

    return 1


def is_aliquot(a, x):
    return x % a == 0 and x / a > 1


def jumps(i, end, num_jump = 0):
    global t
    if i == end:
        return num_jump

    for jump in range(end - i, 1, -1):
        if is_prime(jump) and is_aliquot(jump, t[i]):
            return jumps(i+jump, end, num_jump + 1)

    return -1



t = [4, 4, 9, 0, 0, 0, 0]
print(jumps(0, len(t)-1))